from django import forms
from django.forms import ModelForm
from .models import Athlete
class Athleteform(forms.ModelForm):
    class Meta:
        model = Athlete
        field = ["firstname, lastname, phonenumber, name_spaort, birth_data, visit_first_date,male, famale, age,"
                 "skill, name_skill, profil"]