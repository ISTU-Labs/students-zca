from components import Student, Group, Faculty
from interfaces import IGroup, IStudent, IFaculty
# nose - Библиотека и инструментарий тестирования.
from nose.tools import raises
from storage.components import SQLiteStorage


# implement - реализовать (классам)
# provide - (обеспечивать, оснащать, обслуживать) (экз. класса).


class TestBasics:
    def setUp(self):
        self.student = Student('Черкашин Евгений', '123123')
        self.group = Group("Электронно-вычислительные машины-1992-2",
                      "ЭВМ-91-2")
        self.faculy = Faculty("Институт высоких технологий", "ИВТ")

    def test_student_class_implements(self):
        assert IStudent.implementedBy(Student)

    def test_student(self):
        student = self.student
        assert IStudent.providedBy(student)

    def test_group_clas_implements(self):
        assert IGroup.implementedBy(Group)

    def test_gr_st(self):
        assert IGroup.providedBy(self.group)
        self.group.add_student(self.student)

    @raises(AssertionError)
    def test_bad_addition(self):

        class Cat:
            def __init__(self, name):
                pass

        self.group.add_student(Cat("Butsy"))


class TestSQLiteStuff:
    def setUp(self):
        self.storage = SQLiteStorage("TestDB.sqlite3")
        self.student = Student('Черкашин Евгений', '123123')

    def test_store_student(self):
        self.storage.store(self.student)
