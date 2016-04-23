
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from models import Student, Classroom
from forms import AccountForm
import page_utils

def register(request):
    if request.method == 'POST':
        print request.POST
        acct_form = AccountForm(request.POST)

        if acct_form.is_valid():
            #create user
            username = acct_form.cleaned_data['username']
            email = acct_form.cleaned_data['email']
            password = acct_form.cleaned_data['password1']
            user = User.objects.create_user(username, email, password)
            user.save()

        else: 
            response = {}
            response['errors'] = acct_form.errors
            print acct_form.errors
            return JsonResponse(response, safe=False)

    return HttpResponse(status=200)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, **kwargs):
        context = self.get_context_data()
        context['user_obj'] = request.user
        return render_to_response(self.template_name, context, RequestContext(request))


class StudentView(LoginRequiredMixin, TemplateView):
    template_name = 'student-detail.html'

    def get(self, request, **kwargs):
        student_obj = get_object_or_404(Student, id=kwargs['student_id'])
        context = self.get_context_data()
        context['student'] = student_obj
        return render_to_response(self.template_name, context, RequestContext(request))


class ClassroomView(LoginRequiredMixin, TemplateView):
    template_name = 'class-detail.html'

    def get(self, request, **kwargs):
        class_obj = get_object_or_404(Classroom, id=kwargs['class_id'])
        context = self.get_context_data()

        if request.user.id == class_obj.teacher.id:
            context['current_teacher'] = 'you!'
            context['can_edit'] = True
        else:
            context['current_teacher'] = class_obj.teacher.username
            context['can_edit'] = False
        
        context['class'] = class_obj
        return render_to_response(self.template_name, context, RequestContext(request))


class MyStudentsView(LoginRequiredMixin, TemplateView):
    template_name = 'my-students.html'

    def get(self, request, **kwargs):
        context = self.get_context_data()
        context['students'] = page_utils.list_students_of_teacher(request.user)

        return render_to_response(self.template_name, context, RequestContext(request))

class MyClassroomsView(LoginRequiredMixin, TemplateView):
    template_name = 'my-classrooms.html'

    def get(self, request, **kwargs):
        
        context = self.get_context_data()
        context['classes'] = page_utils.list_classrooms(request.user)

        return render_to_response(self.template_name, context, RequestContext(request))
        
class CreateClassroomView(LoginRequiredMixin, TemplateView):
    template_name = 'create-classroom.html'
    def get(self, request, **kwargs):
        context = self.get_context_data()
        context['students'] = Student.objects.all().order_by('last_name')
        return render_to_response(self.template_name, context, RequestContext(request))

    def post(self, request, **kwargs):
        context = self.get_context_data()
        

def submit_stuff(request):
    if request.method == 'POST':
        print request.POST
    return redirect('/class/1/')
