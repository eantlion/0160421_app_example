from django.contrib import admin
from .models import Student, Classroom



class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]

admin.site.register(Student, StudentAdmin)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["subject_title", "teacher"]

admin.site.register(Classroom, ClassroomAdmin)