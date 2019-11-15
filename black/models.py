from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    track = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    track = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Assignment(models.Model):
    title = models.CharField(max_length=150)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class GradedAssignment(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment,on_delete=models.SET_NULL,blank=True,null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student.username
class Choice(models.Model):   
    title = models.CharField(max_length=187)
    def __str__(self):
        return self.title
class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='answer')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='questions')
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question
