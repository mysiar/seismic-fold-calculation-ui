from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings
from ui.UISettingsDlg import Ui_Settings
import app.app_settings as app_settings


class SettingsDlg(QDialog):
    def __init__(self, settings: QSettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.__settings_read()

        self.ui.create_db_table.stateChanged.connect(self.__form_changed)
        self.ui.delete_db_table.stateChanged.connect(self.__form_changed)



    def __form_changed(self):
        self.settings.setValue(app_settings.DISABLE_CREATE_TABLE_BTN, self.ui.create_db_table.isChecked())
        self.settings.setValue(app_settings.DISABLE_DELETE_TABLE_BTN, self.ui.delete_db_table.isChecked())

    def __settings_read(self):
        self.ui.create_db_table.setChecked(self.settings.value(app_settings.DISABLE_CREATE_TABLE_BTN, False, type=bool))
        self.ui.delete_db_table.setChecked(self.settings.value(app_settings.DISABLE_DELETE_TABLE_BTN, False, type=bool))
