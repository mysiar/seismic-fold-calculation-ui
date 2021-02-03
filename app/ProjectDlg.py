"""
    Project Dialog
"""
from PyQt5.QtWidgets import QFileDialog, QDialog

from ui.UIProjectDlg import Ui_ProjectDlg
from app import AboutDialog, app_info
from app.file_access import read_dict_from_file, write_dict_to_file

DB_URL = 'db_url'
GRID = 'grid_file'
SPS = 'sps_file'
RPS = 'rps_file'
XPS = 'xps_file'
VERBOSE = 'verbose'
DB_VERBOSE = 'db_verbose'


class ProjectDlg(QDialog):
    """class"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ProjectDlg()
        self.ui.setupUi(self)

        self.setWindowTitle(app_info.TITLE + ' - Project')

        self.ui.new_btn.clicked.connect(self.project_new)
        self.ui.open_btn.clicked.connect(self.project_open)
        self.ui.save_btn.clicked.connect(self.project_save)
        self.ui.save_as_btn.clicked.connect(self.project_save_as)

        self.ui.save_btn.setEnabled(False)
        self.ui.save_as_btn.setEnabled(False)

        self.__project = {}
        self.__project_file = None
        self.__project_changed = False

        # form
        self.ui.db_url.textChanged.connect(self.__form_changed)
        self.ui.db_url.textEdited.connect(self.__form_changed)
        self.ui.grid_file_btn.clicked.connect(self.grid_file_open)
        self.ui.sps_file_btn.clicked.connect(self.sps_file_open)
        self.ui.rps_file_btn.clicked.connect(self.rps_file_open)
        self.ui.xps_file_btn.clicked.connect(self.xps_file_open)
        self.ui.verbose.stateChanged.connect(self.__form_changed)
        self.ui.db_verbose.stateChanged.connect(self.__form_changed)

    def grid_file_open(self):
        """grid_file_open"""
        previous_file = self.ui.grid_file.text()
        file = self.file_open(previous_file, "Grid (*.grid )")
        self.ui.grid_file.setText(file)
        if previous_file != file:
            self.__form_changed()

    def sps_file_open(self):
        """sps_file_open"""
        previous_file = self.ui.grid_file.text()
        file = self.file_open(previous_file, "SPS (*.sps, *.s, *.SPS, *.S )")
        self.ui.sps_file.setText(file)
        if previous_file != file:
            self.__form_changed()

    def rps_file_open(self):
        """rps_file_open"""
        previous_file = self.ui.grid_file.text()
        file = self.file_open(previous_file, "RPS (*.rps, *.r, *.RPS, *.R )")
        self.ui.rps_file.setText(file)
        if previous_file != file:
            self.__form_changed()

    def xps_file_open(self):
        """xps_file_open"""
        previous_file = self.ui.grid_file.text()
        file = self.file_open(previous_file, "XPS (*.xps, *.x, *.XPS, *.X )")
        self.ui.xps_file.setText(file)
        if previous_file != file:
            self.__form_changed()

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

    def project_new(self):
        """project_new"""
        self.__project = {
            DB_URL: "",
            GRID: "",
            SPS: "",
            RPS: "",
            XPS: "",
            VERBOSE: 1,
            DB_VERBOSE: 0
        }

        self.__project_file = None
        self.__project_changed = False

        self.ui.save_btn.setEnabled(True)
        self.ui.db_url.setText('')
        self.ui.grid_file.setText('')
        self.ui.sps_file.setText('')
        self.ui.rps_file.setText('')
        self.ui.xps_file.setText('')
        self.ui.project.setTitle('')
        self.ui.save_btn.setEnabled(False)

    def project_open(self):
        """project_open"""
        previous_file = self.__project_file

        self.__project_file = self.file_open(previous_file, "Project (*.prj )")

        if not self.__project_file:
            self.__project_file = previous_file
            return

        self.project_read_from_file()
        self.ui.save_as_btn.setEnabled(True)
        self.ui.project.setTitle(self.__project_file)

    def project_read_from_file(self):
        """project_read_from_file"""
        result = read_dict_from_file(self.__project_file)
        self.ui.db_url.setText(result[DB_URL])
        self.ui.grid_file.setText(result[GRID])
        self.ui.sps_file.setText(result[SPS])
        self.ui.rps_file.setText(result[RPS])
        self.ui.xps_file.setText(result[XPS])
        self.ui.verbose.setChecked(bool(result[VERBOSE]))
        self.ui.db_verbose.setChecked(bool(result[DB_VERBOSE]))

    def project_save_to_file(self):
        """project_save_to_file"""
        project = {
            DB_URL: self.ui.db_url.text(),
            GRID: self.ui.grid_file.text(),
            SPS: self.ui.sps_file.text(),
            RPS: self.ui.rps_file.text(),
            XPS: self.ui.xps_file.text(),
            VERBOSE: int(self.ui.verbose.isChecked()),
            DB_VERBOSE: int(self.ui.db_verbose.isChecked())
        }
        write_dict_to_file(self.__project_file, project)

    def project_save(self):
        """project_save"""
        if not self.__project_file:
            self.project_save_as()
        else:
            self.project_save_to_file()

    def project_save_as(self):
        """project_save_as"""
        project_file, _ = QFileDialog.getSaveFileName(
            self,
            "Save as file",
            "",
            "Project (*.prj );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not project_file:
            return

        self.__project_file = project_file
        self.project_save_to_file()
        self.ui.project.setTitle(self.__project_file)

    def __form_changed(self):
        self.ui.save_btn.setEnabled(True)
        self.__project_changed = True
