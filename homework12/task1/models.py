import datetime

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Student(User):
    pass


class Teacher(User):
    pass


class Homework(models.Model):
    text = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField()

    @classmethod
    def create(cls, text, deadline: datetime.timedelta):
        current_time = datetime.datetime.now()
        return cls(
            text=text,
            deadline=current_time + deadline,
            created=current_time
        )


class HomeworkResult(models.Model):
    solution = models.CharField(max_length=100)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField()
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)

    @classmethod
    def create(cls, solution: str, author: Student, homework: Homework):
        current_time = datetime.datetime.now()
        return cls(
            solution=solution,
            author=author,
            created=current_time,
            homework=homework,
        )
