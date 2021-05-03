from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import addadvisor,appointment



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AdvisorForm(ModelForm):
    class Meta:
        model = addadvisor
        fields = ['advisorname','advisorphotourl']

class AppointmentForm(ModelForm):
    class Meta:
        model = appointment
        fields = ['advisor','date']