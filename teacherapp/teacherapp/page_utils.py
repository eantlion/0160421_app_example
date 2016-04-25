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
	student_qset = Student.objects.filter(classes__in=classroom_qset).order_by('last_name').distinct()
	return student_qset

#Input: Classroom model object
#Output: Queryset containing students not currently in Classroom in order by last name
def list_students_not_enrolled(classroom):
	student_qset =  Student.objects.all().order_by('last_name').exclude(id__in=classroom.students.all().distinct())
	return student_qset
