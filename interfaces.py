from zope.interface import Interface, Attribute

class IStudent(Interface):
    """
    Интерфейс компонент, представляющих студентов
    """

    name = Attribute("Имя студента")
    code = Attribute("Номер зачетки")
    group = Attribute("Группа, к которой приписан студент или None")

    def add_to_group(group):
        """Добавляет студента в группу
        """

    def has_group():
        """Does the student belong to a group
        """

    def __str__():
        """Returns string representation of
        the student
        """

class IGroup(Interface):
    """
    Интерфейс компонент - групп студентов
    """

    def add_student(student):
        """
        Add a student to the group
        """

    def __str__():
        """Return string representastion of the
        group

    """

class IFaculty(Interface):
    def add_group(group):
        """Adds a group to the faculty."""

    def print_groups():
        """Print list of groups."""



