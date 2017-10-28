from django import forms
from django.forms import ModelForm
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Athlete,Sport,Skill

class form_athlete(forms.ModelForm):
    class Meta:
        model=Athlete
        #model=Sport
        #model=Skill
        fields = ['firstname', 'lastename', 'phonenumber','birth_data', 'visit_first_date',
                  'male', 'famale', 'age', 'name_skill', 'profil']
        #fields = ['firstname', 'lastename', 'phonenumber', ' namesport', 'birth_data', ' visit_first_date',
                  #                  # 'male','famale','age',' skill','name_skill','profil']
    firstname = forms.CharField(max_length=30, label="firsname")
    lastename = forms.CharField(max_length=30, label="lastname",required=False)
    phonenumber = forms.CharField(max_length=50, label="phone number",required=False)
    namesport = forms.ModelChoiceField(label="Sport", queryset=Sport.objects.all())
    #def get_now():
     #   return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    birth_data = forms.DateField(required=False)
    visit_first_date = forms.DateField(required=False)
    male = forms.BooleanField(label="male" ,required=False)
    famale = forms.BooleanField(label="fmale",required=False)
    age = forms.IntegerField(label="age")
    skill = forms.ModelChoiceField(label="Skill",queryset=Skill.objects.all())
    name_skill = forms.CharField(max_length=50, label="name skill",required=False)
    profil = forms.CharField(max_length=300, label="profil",required=False)
