from zope.interface import Interface

class IStudent(Interface):
    """
    Интерфейс компонент, представляющих студентов
    """
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
