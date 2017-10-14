from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
class Sport(models.Model):
    id_sport = models.CharField(max_length=50, verbose_name="id_sport")
    name_sport = models.CharField(verbose_name="sportname", max_length=40)
    def __str__(self):
        return self.name_sport

@python_2_unicode_compatible
class Athlete(models.Model):
    id_athlete = models.CharField(max_length=30, verbose_name="id_athlate")
    firstname = models.CharField(max_length=50, verbose_name="firstname")
    lasttname = models.CharField(max_length=50, verbose_name="lastname")
    phonenumber = models.CharField(max_length=50, verbose_name="phonenumber")
    app_sport = models.ForeignKey('Sport')
    birth_date = models.DateTimeField(verbose_name=" Date of Birthday ", null=True, default=None, blank=True)
    visit_first_date = models.DateTimeField(verbose_name=" visit_first_date ", null=True, default=None, blank=True)
    sex = models.ForeignKey('Sex')
    age = models.IntegerField(verbose_name="age", default=0)
    skill = models.ForeignKey('Skill')
    profill = models.CharField(max_length=400, verbose_name="profill")
    def __str__(self):
        return self.lasttname


@python_2_unicode_compatible
class Sex(models.Model):
    id_sex = models.CharField(max_length=50, verbose_name="id_sex")
    type_sex = models.CharField(max_length=10, verbose_name="sex")
    def __str__(self):
       return self.type_sex
@python_2_unicode_compatible
class Skill(models.Model):
    id_skill = models.CharField(max_length=50, verbose_name="id_skill")
    skill_level = models.CharField(max_length=100, verbose_name="skill_level")
    def __str__(self):
        return self.skill_level
'''
@python_2_unicode_compatible
class Supervisor(models.Model):
    #specialisation = models.CharField(max_length=50, verbose_name="Specialisation")
    #fname = models.CharField(max_length=50, verbose_name="fname")
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Developer(models.Model):
    fdname = models.ForeignKey('Supervisor')
    name = models.CharField(max_length=50, verbose_name="name")
    family = models.CharField(max_length=50, verbose_name="family")

    def __str__(self):
        return self.name'''