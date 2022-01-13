from datetime import timedelta

from homework5.task1 import Student, Teacher

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')


def test_classes_t_s_attributes():
    """Testing that classes Teacher and Student elements
     attributes saved properly."""
    assert teacher.last_name == 'Shadrin' and student.first_name == "Roman"


expired_homework = Teacher.create_homework('Learn functions', 0)


def test_classes_hw_attributes():
    """Testing that method create_homework saves in element
    expired_homework attributes properly."""
    assert expired_homework.deadline == timedelta(days=0) and\
           expired_homework.text == "Learn functions"


def test_class_stu_method(capsys):
    """Testing that method do_homework properly checks if HW
    is expired."""
    Student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert Student.do_homework(expired_homework) is None and\
           captured.out.startswith("You're late")
