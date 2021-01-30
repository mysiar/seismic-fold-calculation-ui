from PyQt5.QtCore import QThread, pyqtSignal
from SeismicFoldDbGisUi.FoldDbGisUi import FoldDbGisUi


class FoldUploadThread(FoldDbGisUi, QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    number_of_records = pyqtSignal(int)
    loading = pyqtSignal(str)
    part_done = pyqtSignal()

    def __init__(self, db_engine, csv_file: str, commit_every=10000):
        FoldDbGisUi.__init__(self, db_engine=db_engine, commit_every=commit_every)
        QThread.__init__(self)
        self.__csv_file = csv_file

    def run(self):
        """functionality to update fold from CSV to db"""
