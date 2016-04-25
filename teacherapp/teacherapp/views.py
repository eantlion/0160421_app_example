from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from models import Student, Classroom
from forms import AccountForm, StudentForm, ClassroomForm
import page_utils


def register(request):
    if request.method == 'POST':
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
        class_form = ClassroomForm(request.POST)

        if class_form.is_valid():
            new_class = Classroom.objects.create(
                subject_title = class_form.cleaned_data['subject_title'],
                teacher = request.user)
            new_class.save()
            for student_id in request.POST.getlist('students'):
                new_class.students.add(Student.objects.get(id=student_id))

            return redirect('/class/'+str(new_class.id)+'/')

        else:
            context['errors'] = class_form.errors

        context['students'] = Student.objects.all().order_by('last_name')
        return render_to_response(self.template_name, context, RequestContext(request))


class CreateStudentView(LoginRequiredMixin, TemplateView):
    template_name = 'create-student.html'

    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render_to_response(self.template_name, context, RequestContext(request))

    def post(self, request, **kwargs):
        context = self.get_context_data()
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            new_student = Student.objects.create(
                first_name = student_form.cleaned_data['first_name'],
                last_name = student_form.cleaned_data['last_name'],
                email = student_form.cleaned_data['email'])
            new_student.save()

            return redirect('/student/'+str(new_student.id)+'/')

        else:
            context['errors'] = student_form.errors

        return render_to_response(self.template_name, context, RequestContext(request))


class EditClassroomView(LoginRequiredMixin, TemplateView):
    template_name = 'edit-classroom.html'

    def get(self, request, **kwargs):
        class_obj = get_object_or_404(Classroom, id=kwargs['class_id'])
        if class_obj.teacher != request.user:
            raise Http404("Page does not exist")

        context = self.get_context_data()
        context['class'] = class_obj
        context['current_students'] = class_obj.students.all()
        context['new_students'] = Student.objects.all().order_by('last_name').exclude(id__in=class_obj.students.all().distinct())
        
        return render_to_response(self.template_name, context, RequestContext(request))

    def post(self, request, **kwargs):  
        class_obj = get_object_or_404(Classroom, id=kwargs['class_id'])
        if class_obj.teacher != request.user:
            raise Http404("Page does not exist")

        for student_id in request.POST.getlist('remove_students'):
            class_obj.students.remove(Student.objects.get(id=student_id))

        for student_id in request.POST.getlist('add_students'):
            class_obj.students.add(Student.objects.get(id=student_id))

        context = self.get_context_data()
        context['class'] = class_obj
        context['current_students'] = class_obj.students.all()
        context['new_students'] = Student.objects.all().order_by('last_name').exclude(id__in=class_obj.students.all().distinct())
        return render_to_response(self.template_name, context, RequestContext(request))