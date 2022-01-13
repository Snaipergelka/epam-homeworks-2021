import datetime

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Student(User):
    def __str__(self):
        return f"Student({self.first_name} {self.last_name})"


class Teacher(User):
    def __str__(self):
        return f"Teacher({self.first_name} {self.last_name})"


class Homework(models.Model):
    text = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"Homework(Teacher: {self.teacher} Text:{self.text} " \
               f"Create: {self.created} Deadline: {self.deadline} )"

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

    def __str__(self):
        return f"HomeworkResult(Homework: {self.homework}, " \
               f"Author: {self.author}, " \
               f"Date: {self.created}, " \
               f"Solution: {self.solution})"

    @classmethod
    def create(cls, solution: str, author: Student, homework: Homework):
        current_time = datetime.datetime.now()
        return cls(
            solution=solution,
            author=author,
            created=current_time,
            homework=homework,
        )
