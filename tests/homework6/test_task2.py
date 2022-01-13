from homework6.task2 import Student, Teacher

opp_teacher = Teacher('Daniil', 'Shadrin')
advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

lazy_student = Student('Roman', 'Petrov')
good_student = Student('Lev', 'Sokolov')

oop_hw = opp_teacher.create_homework('Learn OOP', 1)
docs_hw = opp_teacher.create_homework('Read docs', 5)

result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
result_3 = lazy_student.do_homework(docs_hw, 'done')


def test_homework_done():
    """Testing that homework_done saves homework results without doubling,
    and also is accessible to class Teacher."""
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


opp_teacher.check_homework(result_2)


def test_check_homework_method():
    """Testing that check_homework method checks len of homework"""
    temp = opp_teacher.check_homework(result_3)
    assert not temp


def test_reset_results():
    """Testing that resetting results deletes only results we need"""
    Teacher.reset_results(homework=docs_hw)
    assert Teacher.homework_done[docs_hw] == set()
