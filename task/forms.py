from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Athlete,Sport,Skill
from django.core.exceptions import ValidationError
from django.contrib import messages

class form_athlete(forms.ModelForm):
    class Meta:
        model= Athlete
        model= Sport
        model= Skill
        fields = ['firstname', 'lastename', 'phonenumber','namesport','birth_data', 'visit_first_date',
                  'male', 'famale', 'age','skill', 'name_skill', 'profil']
    firstname = forms.CharField(max_length=30, label="firsname",required=False,validators=[RegexValidator(r'\w')])
    lastename = forms.CharField(max_length=30, label="lastname",required=False)
    phonenumber = forms.CharField(max_length=10,min_length=10,validators = [RegexValidator(r'\d{10}')])
    #validators = [RegexValidator(r'\d{10}+|\d{5}([- ]*)\d{6}')]
    namesport = forms.ModelChoiceField(label="Sport", queryset=Sport.objects.all())
    birth_data = forms.DateField(required=False)
    visit_first_date = forms.DateField(required=False)
    male = forms.BooleanField(label="male" ,required=False)
    famale = forms.BooleanField(label="fmale",required=False)
    age = forms.IntegerField(label="age")
    skill = forms.ModelChoiceField(label="Skill",queryset=Skill.objects.all())
    name_skill = forms.CharField(max_length=50, label="name skill",required=False)
    profil = forms.CharField(max_length=300, label="profil",required=False)


    def get_due_date(self):

        diff = self.cleaned_data['birth_data'] - datetime.date.today()

        if diff.days < 0:
            raise ValidationError("Please enter valid date. Either today's date or after that.")

        else:

             return self.cleaned_data['birth_data']
    def get_number(self):
        phonenumber=self.cleaned_data['phonenumber']
        if len(phonenumber) < 10:
            raise forms.ValidationError("Headline must be more than 9 characters.")
        else:
            return phonenumber


