import csv
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QTextBrowser, QProgressBar

from SeismicFoldDbGisUi.entity.Bin import Bin


class FoldDbGisUi:

    def __init__(self, db_engine, output: QTextBrowser, progress_bar: QProgressBar, commit_every=10000):
        self.__db_engine = db_engine
        self.__commit_every = commit_every
        self.__output = output
        self.__progress_bar = progress_bar

    def create_table(self):
        Bin.__table__.create(self.__db_engine)

    def delete_table(self):
        # Bin.__table__.drop(self.__db_engine)
        Bin.__table__.drop(self.__db_engine)

    def load_from_csv(self, filename: str):
        """
        load from CSV with columns ['Easting', 'Northing', 'Fold', 'Bin Number', 'Row', 'Column']
        """
        number_of_records = FoldDbGisUi.__count_file_line_number(filename)
        self.__progress_bar.setMinimum(1)
        self.__progress_bar.setMaximum(number_of_records)
        _session = self.__create_session()
        counter = 1
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for record in csv_reader:
                bin = FoldDbGisUi.__create_bin_from_csv_record(record)
                _session.add(bin)
                if counter % self.__commit_every == 0:
                    self.__output.append("{:15,d}".format(counter))
                    _session.commit()
                self.__progress_bar.setValue(counter)
                counter += 1

            self.__output.append("{:15,d}".format(counter))
            self.__progress_bar.setValue(counter)
            _session.commit()
        _session.close()

    def update_from_csv(self, filename: str):
        """
        update from CSV with columns ['Easting', 'Northing', 'Fold', 'Bin Number', 'Row', 'Column']
        """
        number_of_records = FoldDbGisUi.__count_file_line_number(filename)
        self.__progress_bar.setMinimum(1)
        self.__progress_bar.setMaximum(number_of_records)
        _session = self.__create_session()
        counter = 1
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for record in csv_reader:
                binn = int(record[3])
                b = _session.query(Bin).filter_by(binn=binn).first()

                if b is not None:
                    b.fold = b.fold + int(record[2])
                else:
                    b = FoldDbGisUi.__create_bin_from_csv_record(record)
                    _session.add(b)

                if counter % self.__commit_every == 0:
                    self.__output.append("{:15,d}".format(counter))
                    _session.commit()
                self.__progress_bar.setValue(counter)
                counter += 1

            self.__output.append("{:15,d}".format(counter))
            self.__progress_bar.setValue(counter)
            _session.commit()
        _session.close()

    @staticmethod
    def __create_bin_from_csv_record(record: list):
        b = Bin(
            binn=int(record[3]),
            fold=int(record[2]),
            geom="POINT (%.1f %.1f)" % (float(record[0]), float(record[1]))
        )

        return b

    def __create_session(self):
        sess_mkr = sessionmaker()
        sess_mkr.configure(bind=self.__db_engine)
        return sess_mkr()

    @staticmethod
    def __count_file_line_number(filename: str):
        return sum(1 for line in open(filename))
