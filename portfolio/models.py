from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Person(models.Model):

    name = models.CharField(max_length=50)
    linkdin = models.URLField()
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Teacher(Person,models.Model):
    lusofona_url = models.URLField()

class Student(Person,models.Model):

    portfolio = models.URLField()
    github = models.URLField()

class Project(models.Model):

    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500)
    #image = models.ImageField()
    year = models.IntegerField(default=0)
    github = models.URLField()
    video_url = models.URLField()
    tech = models.CharField(max_length=200)
    skills = models.CharField(max_length=500)
    participants = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Subject(models.Model):

    name = models.CharField(max_length=30)
    year = models.IntegerField(default=0)
    etcs = models.IntegerField(default=0)
    semester = models.IntegerField(default=0)
    school_year = models.IntegerField(default=0)
    rank = models.IntegerField(default=0, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    topics = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank = True)
    teacher = models.ManyToManyField(Teacher, blank = True)
    #subject_project = models.OneToOneField(Project,on_delete=models.CASCADE,primary_key=True,)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title + ' from ' + str(self.author)


class Answer(models.Model):
    answer_text = models.CharField(max_length = 255)
    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

class Question(models.Model):
    question_text = models.CharField(max_length = 255)
    points = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question_text

class Quizz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


        
    
