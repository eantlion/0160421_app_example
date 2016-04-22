
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.models import User

from forms import AccountForm

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

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render_to_response(self.template_name, context, RequestContext(request))

class StudentView(TemplateView):
    template_name = 'student-detail.html'

    def get(self, request, **kwargs):
        print kwargs
        context = self.get_context_data()
        return render_to_response(self.template_name, context, RequestContext(request))
