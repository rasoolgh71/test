from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Athlete, Skill, Sport

class form_athlete(forms.Form):
    firstname = forms.CharField(max_length=30, label="firsname")
    lastename = forms.CharField(max_length=30, label="lastname")
    phonenumber = forms.CharField(max_length=50, label="phone number",required=False)
    namesport = forms.ModelChoiceField(label="Sport", queryset=Sport.objects.all())
    birth_data = forms.DateTimeField(label="date of birthday")
    visit_first_date = forms.DateTimeField(label=" visit first date")
    male = forms.BooleanField(label="male",required=False)
    famale = forms.BooleanField(label="fmale",required=False)
    age = forms.IntegerField(label="age")
    skill = forms.ModelChoiceField(label="Skill",queryset=Skill.objects.all())
    name_skill = forms.CharField(max_length=50, label="name skill",required=False)
    profil = forms.CharField(max_length=300, label="profil",required=False)
