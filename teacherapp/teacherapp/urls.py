"""teacherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views
import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/', 
        auth_views.login, 
        {'template_name': 'login.html'}),

    url(r'^register/submit/', 
        app_views.register, 
        name='register'),

    url(r'^accounts/profile/', 
        app_views.DashboardView.as_view(), 
        name='profile'),

    url(r'^student/(?P<student_id>[0-9]{1,64})/$',
        app_views.StudentView.as_view(),
        name="student_details"),

    url(r'^class/(?P<class_id>[0-9]{1,64})/$',
        app_views.ClassroomView.as_view(),
        name="class_details"),

    url(r'^mystudents/$',
        app_views.MyStudentsView.as_view(),
        name="my_students"),

    url(r'^myclassrooms/$',
        app_views.MyClassroomsView.as_view(),
        name="my_classrooms"),

    url(r'^create-classroom/', 
        app_views.CreateClassroomView.as_view(), 
        name="create_classroom"),

    url(r'^classroom/submit/', 
        app_views.submit_stuff, 
        name='classroom_submit'),

]
