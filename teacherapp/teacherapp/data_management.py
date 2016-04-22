from models import Student, Classroom
from django.contrib.auth.models import User




#Input: User model object
#Output: list containing all Classroom model objects belonging to user
def list_classrooms(user):
	classroom_set = Classroom.objects.filter(teacher=user)
	return classroom_qset

#Input: User model object
#Output: QuerySet containing all Student model objects present in classrooms belonging to User
def list_students_of_teacher(user):
	classrooms_qset = list_classrooms(user)
	student_qset = Student.objects.filter(students__in=[classrooms_qset]).distinct()
	return student_qset

