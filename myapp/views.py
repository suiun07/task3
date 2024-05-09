from django.shortcuts import render

from myapp.models import Student, Course

student = Student.objects.create(
    first_name='John',
    last_name='Doe',
    email='john@example.com',
    age=25
)

course = Course.objects.create(
    name='Introduction to Django',
    description='A beginner course on Django web framework'
)

course.students.add(student)

