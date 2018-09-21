import sqlite3
import os.path
import sys

class Sqlite:
    _file_db = None
    _conn = None

    def __init__(self, file_db='temp', auto_conect=True, with_file_existed=True):
        self.setFileDB(file_db)
        if with_file_existed:
            if self.checkFile():
                print("DB file not found!")
                sys.exit(1)
        if auto_conect:
            self.conection()

    def checkFile(self):
        os.path.isfile(self._file_db)

    def setFileDB(self, file_db):
        self._file_db = file_db

    def conection(self):
        self._conn = sqlite3.connect(self._file_db)

    def getInfo(self, query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        return cursor

    def setInfo(self, query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        return self._conn.commit()

    def closeConection(self):
        self._conn.close()
