import datetime
from django.contrib import admin
from .models import Patient, Question, Fields, Complaint
from django.forms import ModelForm, ModelChoiceField
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Option
from django.db import models


def i18n_javascript(request):
    return admin.site.i18n_javascript(request)


class PatientForm(ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', widget=AdminDateWidget())

    class Meta:
        model = Patient
        fields = ('__all__')


class OptionForm(ModelForm):
    series = ModelChoiceField(label='Ответ', queryset=Option.objects.all())
    pat = ModelChoiceField(label='Пациент', queryset=Patient.objects.order_by('name'))

    class Meta:
        model = Complaint
        fields = ('__all__')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Электронная почта:', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
