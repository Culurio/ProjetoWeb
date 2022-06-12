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

class Skills(models.Model):
    name = models.CharField(max_length=50)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Project(models.Model):

    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='pictures/', blank=True)
    year = models.IntegerField(default=0)
    school_year = models.IntegerField(default=0)
    github = models.URLField()
    video_url = models.URLField()
    participants = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Project_small(Project,models.Model):
    tech = models.CharField(max_length=200)
    skills =  models.ManyToManyField(Skills, related_name='teacher')
    teacher = models.ManyToManyField(Teacher, related_name='teacher')

    def __str__(self):
        return self.title

class Project_big(Project,models.Model):
    report = models.URLField()
    teacher = models.ManyToManyField(Teacher, related_name='advisor')

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
    teacher_theory = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacher_practice = models.ManyToManyField(Teacher, related_name='practice_teacher')
    subject_project = models.OneToOneField(Project_small,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_image = models.ImageField(upload_to='pictures/', blank=True)
    post_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title + ' from ' + str(self.author)

class Quizz(models.Model):
    name = models.CharField(max_length=20)    
    surname = models.CharField(max_length=20)     
    points = models.IntegerField()


    def __str__(self):
        return self.name


        
    
