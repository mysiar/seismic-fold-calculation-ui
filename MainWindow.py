from PyQt5.QtWidgets import QMainWindow, QFileDialog
import webbrowser
import json

from UIMainWindowForm import Ui_MainWindow
import AboutDialog
import app_info


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew_project.triggered.connect(self.project_new)
        self.ui.actionOpen_project.triggered.connect(self.project_open)
        self.ui.actionSave_project.triggered.connect(self.project_save)
        self.ui.actionSave_as_project.triggered.connect(self.project_save_as)
        self.ui.actionQuit.triggered.connect(self.quit)

        self.ui.actionLicense.triggered.connect(self.help_license)
        self.ui.actionAbout.triggered.connect(self.help_about)

        self.ui.actionSave_project.setEnabled(False)
        self.ui.actionSave_as_project.setEnabled(False)

        self.__project = {}
        self.__project_file = None

        self.__db_url = ""
        self.__grid_file = ""
        self.__sps_file = ""
        self.__rps_file = ""
        self.__xps_file = ""
        self.__verbose = 1
        self.__db_verbose = 0

    def project_new(self):
        self.__project = {
            "db_url": self.__db_url,
            "grid_file": self.__grid_file,
            "sps_file": self.__sps_file,
            "rps_file": self.__rps_file,
            "xps_file": self.__xps_file,
            "verbose": self.__verbose,
            "db_verbose": self.__db_verbose
        }

        self.ui.actionSave_as_project.setEnabled(True)
        self.__project_file = None

    def project_open(self):
        previous_file = self.__project_file

        self.__project_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Project (*.prj );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.__project_file:
            self.__project_file = previous_file
            return

        self.project_read_from_file()

    def project_read_from_file(self):
        pass

    def project_save_to_file(self):
        file = open(self.__project_file, 'w')
        json.dump(self.__project, file)
        file.close()

    def project_save(self):
        pass

    def project_save_as(self):
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

    @staticmethod
    def help_license():
        webbrowser.open(app_info.LICENSE_URL)

    def help_about(self):
        """
            Displays Application About Dialog
        """
        dlg = AboutDialog.AboutDialog()
        dlg.exec_()

    def quit(self):
        self.close()
