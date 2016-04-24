from django import forms
from django.contrib.auth.models import User

class AccountForm(forms.Form):
    #This class is being used purely for serverside validation
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(max_length=64, required=True)
    password2 = forms.CharField(max_length=64, required=True)

    def clean_username(self):
        # check if username does not exist yet
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is taken already",code="duplicate")

    def clean_password2(self): # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data: #check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
                raise forms.ValidationError("Passwords don't match", code="mismatch")
        return self.cleaned_data['password2']

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

class ClassroomForm(forms.Form):
    subject_title = forms.CharField(max_length=64, required=True)