"""
    MainWindow
"""
import webbrowser
import logging
from importlib import reload
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import Qt, QSettings
from sqlalchemy import create_engine
from sqlalchemy.event import listen

from FixedWidthTextParser.Seismic.SpsParser import Sps21Parser
from SeismicFoldUi.Grid import Grid
from SeismicFoldUi.FoldUi import FoldUi
from SeismicFoldDbGisUi.FoldDbGisUi import FoldDbGisUi
from SeismicFoldDbGisUi.FoldLoadThread import FoldLoadThread
from SeismicFoldDbGisUi.FoldUpdateThread import FoldUpdateThread

from ui.UIMainWindowForm import Ui_MainWindow
from app.ProjectDlg import ProjectDlg
from app.SettingsDlg import SettingsDlg
import app.AboutDialog
import app.app_info
import app.app_settings as app_settings
from app.file_access import read_dict_from_file

DB_URL = 'db_url'
GRID = 'grid_file'
SPS = 'sps_file'
RPS = 'rps_file'
XPS = 'xps_file'
FOLD = 'fold_file'
VERBOSE = 'verbose'
DB_VERBOSE = 'db_verbose'
POSTGRES = 'postgresql'
SQLITE = 'sqlite'
SPATIALITE_EXT = '/usr/lib/x86_64-linux-gnu/mod_spatialite.so'


class MainWindow(QMainWindow):
    """class"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QSettings(app_settings.ORG, app_settings.APP)
        self.__settings_read()

        self.setWindowTitle(app.app_info.TITLE)

        # menu
        self.ui.actionOpen_project.triggered.connect(self.project_open)
        self.ui.actionSettings.triggered.connect(self.action_settings)
        self.ui.actionQuit.triggered.connect(self.quit)

        self.ui.action_project.triggered.connect(self.action_project)

        self.ui.actionLicense.triggered.connect(self.help_license)
        self.ui.actionAbout.triggered.connect(self.help_about)

        self.ui.db_table_create_btn.clicked.connect(self.action_db_table_create)
        self.ui.db_table_delete_btn.clicked.connect(self.action_db_table_delete)
        self.ui.fold_calculate_btn.clicked.connect(self.action_fold_calculate)
        self.ui.fold_load_btn.clicked.connect(self.action_fold_load)
        self.ui.fold_update_btn.clicked.connect(self.action_fold_update)

        self.__project_file = None

        self.worker = None

        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint & ~Qt.WindowMaximizeButtonHint)
        self.__enable_ui(False)
        self.ui.menu_file.setEnabled(True)

    def __enable_ui(self, enable: bool):
        self.ui.fold_calculate_btn.setEnabled(enable)
        self.ui.fold_load_btn.setEnabled(enable)
        self.ui.fold_update_btn.setEnabled(enable)
        self.ui.menu_file.setEnabled(enable)
        if enable is False:
            self.ui.db_table_create_btn.setEnabled(enable)
            self.ui.db_table_delete_btn.setEnabled(enable)
        else:
            self.__enable_ui_on_settings()

    def __enable_ui_on_settings(self):
        self.ui.db_table_create_btn.setEnabled(
            not self.settings.value(app_settings.DISABLE_CREATE_TABLE_BTN, type=bool))
        self.ui.db_table_delete_btn.setEnabled(
            not self.settings.value(app_settings.DISABLE_DELETE_TABLE_BTN, type=bool))

    def action_db_table_create(self):
        self.__enable_ui(False)
        try:
            engine = self._create_db_engine(db_url=self.ui.db_url.text(), db_verbose=self.ui.db_verbose.isChecked())
            fold = FoldDbGisUi(db_engine=engine)
            fold.create_table()
            self.__log('Table created.')

        except Exception as e:
            self.__log(str(e))
        self.__enable_ui(True)
        self.end_of_proc()

    def action_db_table_delete(self):
        self.__enable_ui(False)
        try:
            engine = self._create_db_engine(db_url=self.ui.db_url.text(), db_verbose=self.ui.db_verbose.isChecked())
            fold = FoldDbGisUi(db_engine=engine)
            fold.delete_table()
            self.__log('Table deleted.')
        except Exception as e:
            self.__log(str(e))
        self.__enable_ui(True)
        self.end_of_proc()

    def action_fold_calculate(self):
        """calculate fold"""
        # try:
        parser = Sps21Parser()
        grid = Grid()
        grid.read(self.ui.grid_file.text())

        self.__enable_ui(False)
        self.worker = FoldUi(
            grid=grid,
            parser=parser,
            sps_file=self.ui.sps_file.text(),
            rps_file=self.ui.rps_file.text(),
            xps_file=self.ui.xps_file.text(),
            fold_file=self.ui.fold_file.text(),
        )

        self.worker.progress.connect(self.signal_progress)
        self.worker.number_of_records.connect(self.signal_number_of_records)
        self.worker.loading.connect(self.signal_loading)
        self.worker.part_done.connect(self.end_of_proc)
        self.worker.start()
        self.worker.finished.connect(self.signal_finished)

    def action_fold_load(self):
        """load fold from csv file"""
        self.__enable_ui(False)
        engine = self._create_db_engine(db_url=self.ui.db_url.text(), db_verbose=self.ui.db_verbose.isChecked())
        self.worker = FoldLoadThread(db_engine=engine, csv_file=self.ui.fold_file.text())
        self.worker.progress.connect(self.signal_progress)
        self.worker.number_of_records.connect(self.signal_number_of_records)
        self.worker.loading.connect(self.signal_loading)
        self.worker.part_done.connect(self.end_of_proc)
        self.worker.start()
        self.worker.finished.connect(self.signal_finished)

    def action_fold_update(self):
        """updating fold from csv file"""
        self.__enable_ui(False)
        engine = self._create_db_engine(db_url=self.ui.db_url.text(), db_verbose=self.ui.db_verbose.isChecked())
        self.worker = FoldUpdateThread(db_engine=engine, csv_file=self.ui.fold_file.text())
        self.worker.progress.connect(self.signal_progress)
        self.worker.number_of_records.connect(self.signal_number_of_records)
        self.worker.loading.connect(self.signal_loading)
        self.worker.part_done.connect(self.end_of_proc)
        self.worker.start()
        self.worker.finished.connect(self.signal_finished)

    def project_open(self):
        """project_open"""
        previous_file = self.__project_file

        self.__project_file = self.file_open(previous_file, "Project (*.prj )")

        if not self.__project_file:
            self.__project_file = previous_file
            return

        self.project_read_from_file()
        self.ui.project.setTitle(self.__project_file)
        self.__enable_ui(True)
        self.__prepare_logging()
        logging.info('Project opened')

    def file_open(self, previous_file: str, file_pattern: str):
        """file open - common method to get file name"""
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "{};;All files (*.*)".format(file_pattern),
            # options=QFileDialog.DontUseNativeDialog
        )

        if file not in (previous_file, ''):
            return file
        else:
            return previous_file

    def project_read_from_file(self):
        """project_read_from_file"""
        result = read_dict_from_file(self.__project_file)
        self.ui.db_url.setText(result[DB_URL])
        self.ui.grid_file.setText(result[GRID])
        self.ui.sps_file.setText(result[SPS])
        self.ui.rps_file.setText(result[RPS])
        self.ui.xps_file.setText(result[XPS])
        self.ui.fold_file.setText(result[FOLD])
        self.ui.db_verbose.setChecked(bool(result[DB_VERBOSE]))

    @staticmethod
    def help_license():
        """help_license"""
        webbrowser.open(app.app_info.LICENSE_URL)

    @staticmethod
    def help_about():
        """Displays Application About Dialog"""
        dlg = app.AboutDialog.AboutDialog()
        dlg.exec_()

    def quit(self):
        """close app"""
        self.close()

    @staticmethod
    def _create_db_engine(db_url: str, db_verbose: bool):
        """creates SQLAlchemy engine"""
        db_type = db_url.split(":")[0]
        if POSTGRES == db_type:
            engine = create_engine(db_url, echo=db_verbose)
        elif SQLITE == db_type:
            engine = create_engine(db_url, echo=db_verbose)
            listen(engine, 'connect', MainWindow._load_spatialite)
        else:
            raise Exception('Not supported/tested DB engine: {}'.format(db_type))

        return engine

    # pylint: disable=unused-argument
    @staticmethod
    def _load_spatialite(dbapi_conn, connection_record):
        """ loads spatialite extension"""
        dbapi_conn.enable_load_extension(True)
        dbapi_conn.load_extension(SPATIALITE_EXT)

    @staticmethod
    def timer(start, end):
        """ timer """
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)

    def end_of_proc(self):
        self.ui.output.append('-----------------------------------------------------')
        logging.info('-----------------------------------------------------')

    def signal_progress(self, counter: int):
        self.ui.progress_bar.setValue(counter)

    def signal_number_of_records(self, number_of_records):
        self.__log("Number of records: {:,d}".format(number_of_records))
        self.ui.progress_bar.setMinimum(1)
        self.ui.progress_bar.setMaximum(number_of_records)

    def signal_loading(self, msg: str):
        self.__log(msg)

    def signal_finished(self):
        self.__enable_ui(True)
        self.ui.progress_bar.setValue(1)

    @staticmethod
    def action_project():
        """
            Displays Dialog
        """
        dlg = ProjectDlg()
        dlg.exec_()

    def action_settings(self):
        dlg = SettingsDlg(self.settings)
        dlg.exec_()
        self.__settings_read()

    def __settings_read(self):
        self.ui.db_table_create_btn.setEnabled(
            not self.settings.value(app_settings.DISABLE_CREATE_TABLE_BTN, False, type=bool))
        self.ui.db_table_delete_btn.setEnabled(
            not self.settings.value(app_settings.DISABLE_DELETE_TABLE_BTN, False, type=bool))

    def __prepare_logging(self):
        logging.shutdown()
        reload(logging)
        log_filename = self.__project_file + '.log'
        log_format = '%(asctime)s - %(message)s'
        logging.basicConfig(filename=log_filename, filemode='a', format=log_format, level=logging.INFO)

    def __log(self, msg: str):
        self.ui.output.append(msg)
        logging.info(msg)
