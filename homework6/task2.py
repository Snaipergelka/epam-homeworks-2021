"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from typing import Optional


class Homework:
    """
        Class that creates Homework instance with
        three attributes.
        Attributes:
            text - homework text
            deadline - deadline for homework in days
            created - datetime of creation of hw
        """
    __slots__ = ["text", "deadline", "created"]

    def __init__(self, text: str, deadline: int):
        """
            :param str text: homework text
            :param int|float deadline: homework deadline in days
        """
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self):
        """
            :return: bool if the deadline was expired or not
            :rtype: bool
        """
        return (self.deadline + self.created) > datetime.datetime.today()


class DeadlineError(Exception):
    """
        Class that creates deadline error object.
    """
    pass


class ClassError(Exception):
    """
        Class that creates class error object.
    """
    pass


class HomeworkResult:
    """
        Class that creates Homework result instance with 4 attributes.
        Attributes:
            homework - class Homework instance
            solution - text of homework solution
            author - class Student instance
            created - time of creation
    """
    __slots__ = ["homework", "solution", "author", "created"]

    def __init__(self, homework: Homework, solution: str, author):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ClassError("You gave a not Homework object")
        self.solution = solution
        self.author = author
        self.created = homework.created


class Person:
    """
        Class that creates instance person with two attributes.
        Attributes:
            last_name - person last name
            first_name - person first name
    """
    __slots__ = ["last_name", "first_name"]

    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """
         Class creates Student instance which inherits from
         class Person.
    """
    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        """
            Checks if homework is not expired and creates class HomeworkResult
            instance with homework solution and raises DeadlineError
            otherwise.
            :param Homework homework: class Homework instance
            :param str solution: string solution of homework
            :return: class HomeworkResult instance
            :rtype: HomeworkResult
        """
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You're late")


class Teacher(Person):
    """
        Class creates Teacher instance which inherits from
        class Person.
    """
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
            Creates class Homework instance.
            :param str text: homework text
            :param int|float deadline: homework deadline in days
            :return: class Homework instance
            :rtype: Homework
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result: HomeworkResult):
        """
            Checks if homework result solution is valid by length and adds
            to homework_done dict where key is Homework class instance,
            value is set of HomeworkResult instances.

            :param HomeworkResult homework_result: class HomeworkResult
            instance
            :return: bool if homework result solution is valid by length
            :rtype: bool
        """
        if len(homework_result.solution) > 5:
            if homework_result.homework not in cls.homework_done:
                cls.homework_done[homework_result.homework] = set()
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework: Optional[Homework]):
        """
            Resets homework results dicts if homework parameter is None.
            Resets only homework_done[homework] otherwise.
            :param Homework homework: Homework class instance
        """
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework, None)


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[docs_hw])
    Teacher.reset_results()
