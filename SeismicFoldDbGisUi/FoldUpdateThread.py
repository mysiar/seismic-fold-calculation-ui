import csv
import time
from PyQt5.QtCore import QThread, pyqtSignal
from SeismicFoldDbGisUi.FoldDbGisUi import FoldDbGisUi, Bin


class FoldUpdateThread(FoldDbGisUi, QThread):
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
        """functionality to update fold from CSV in db"""
        try:
            start = time.time()
            self.loading.emit('Updating fold in db')
            number_of_records = self._count_file_line_number(self.__csv_file)
            self.number_of_records.emit(number_of_records)
            _session = self._create_session()
            counter = 1
            with open(self.__csv_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for record in csv_reader:
                    binn = int(record[3])
                    b = _session.query(Bin).filter_by(binn=binn).first()

                    if b is not None:
                        b.fold = b.fold + int(record[2])
                    else:
                        b = FoldDbGisUi._create_bin_from_csv_record(record)
                        _session.add(b)

                    if counter % self._commit_every == 0:
                        _session.commit()
                    self.progress.emit(counter)
                    counter += 1

                self.progress.emit(counter)
                _session.commit()
            _session.close()
            self.loading.emit('Updated in ' + self.timer(start, time.time()))
        except Exception as e:
            self.loading.emit(str(e))

        self.part_done.emit()
        self.finished.emit()
