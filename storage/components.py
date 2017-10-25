from .interfaces import ISQLiteStorage, ISQLiteStorageAdapter
from zope.interface import implementer
from zope.component import getAdapter
import sqlite3
import uuid

implementer(ISQLiteStorage)
class SQLiteStorage:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.create_tables()

    def store(self, obj):
        storer = getAdapter(ISQLiteStorageAdapter, obj)
        return storer.store(store)

    def get(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * from metadata WHERE uuid=?", (id,))
        metadata = cur.fetchone()
        cls = metadata[1]
        stub = globals()[cls].make_stub()

        storer = getAdapter(ISQLiteStorageAdapter, stub)
        storer.retrieve(self)
        return stub

    def create_tables(self):
        conn=self.conn
        tables=["students", "groups"]
        for tbl in tables:
            conn.execute("DROP TABLE IF EXISTS {}".format(tbl))
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                name text,
                code text
                group_id integer
            )""")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                name text,
                code text,
            )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
        uuid text,
        class text,
        table text,
        objrowid int
        )
        """)



class AIStudentToISQLiteStorageAdapter:
    def __init__(self, obj):
        self.obj=obj
    def store(self, storage):
        student = self.obj
        conn = storage.conn
        cur = conn.cursor()
        if hasattr(student, "_rowid"):
            cur.execute("""
            UPDATE students
                SET name = ?,
                    code = ?
            WHERE
                rowid=?
            """, (student.name, student.code, student._rowid))
        else:
            cur.execute("INSERT INTO students VALUES (?,?)",
                        (student.name, student.code))
            rowid = cur.lastrowid
            uu = uuid.uuid1()
            cur.execute("INSERT INTO metadata VALUES (?,?,?,?)",
                        (uu, student.__class__.__name__, "students", rowid)
            )
            student._uuid=uu
            student._rowid=rowid
        return uu


    def retrieve(self, storage):
        pass
