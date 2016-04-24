from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 


class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Classroom(models.Model):
	subject_title = models.CharField(max_length=64)
	teacher = models.ForeignKey(User)
	students = models.ManyToManyField(Student, related_name="classes")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)