from interfaces import IStudent, IGroup, IFaculty
from zope.interface import implementer

class NamedEncodedThing(object):
    def __init__(self, name, code):
        self.name=name
        self.code=code

class NamedEncodedThingWithAListOfThings(NamedEncodedThing):
    def __init__(self, name, code):
        super(NamedEncodedThingWithAListOfThings, self).__init__(name, code)
        self.things=[]

    def _add_thing(self, thing, interface, condition=None, msg=""):
        assert interface.providedBy(thing), "must provide {}".format(interface)
        if condition is not None:
            assert not condition(thing), msg
        self.things.append(thing)

@implementer(IGroup)
class Group(NamedEncodedThingWithAListOfThings):
    def __str__(self):
        s=''
        for student in self.things:
            s+=str(student)+"\n"
        return s

    def add_student(self, student):
        self._add_thing(student, IStudent,
              Student.has_group, "student must not belong to a group")
        student.add_to_group(self)


@implementer(IStudent)
class Student(NamedEncodedThing):
    def __init__(self, name, code):
        super(Student, self).__init__(name,code)
        self.group = None

    def has_group(self):
        return self.group is not None

    def add_to_group(self, group):
        self.group=group

@implementer(IFaculty)
class Faculty(NamedEncodedThingWithAListOfThings):
    def add_group(self, group):
        self._add_thing(group, IFaculty)

    def print_list(self):
        for group in self.things:
            print(group)






