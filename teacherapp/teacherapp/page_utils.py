from models import Student, Classroom
from django.contrib.auth.models import User

#Input: User model object
#Output: list containing all Classroom model objects belonging to user
def list_classrooms(user):
	classroom_qset = Classroom.objects.filter(teacher=user)
	return classroom_qset

#Input: User model object
#Output: QuerySet containing all Student model objects present in classrooms belonging to User
def list_students_of_teacher(user):
	classroom_qset = Classroom.objects.filter(teacher=user)
	student_qset = Student.objects.filter(classes__in=classroom_qset).distinct()
	return student_qset
