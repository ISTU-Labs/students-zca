from .interfaces import ISQLiteStorage, ISQLiteStorageAdapter
from zope.interface import implementer
from zope.component import getAdapter
import sqlite3

implementer(ISQLiteStorage)
class SQLiteStorage:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.create_tables()

    def store(self, obj):
        storer = getAdapter(ISQLiteStorageAdapter, obj)
        return storer.store(store)

    def get(self, id):
        pass
        #storer = getAdapter(ISQLiteStorageAdapter, id)

    def create_tables(self):
        conn=self.conn
        tables=["students", "groups"]
        for tbl in tables:
            conn.execute("DROP TABLE IF EXISTS {}".format(tbl))
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                name text,
                code text
            )""")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                name text,
                code text,
                student_id integer
            )""")


class AIStudentToISQLiteStorageAdapter:
    def __init__(self, obj):
        self.obj=obj
    def store(self, storage):
        student = self.obj
        conn = storage.conn
        cur = conn.cursor()
        cur.execute("INSERT INTO students VALUES (?,?)",
            (student.name, student.code))
        return cur.lastrowid

