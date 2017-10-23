from django.db import models
# Create your models here.
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
class Sport(models.Model):
    name_sport = models.CharField(max_length=50, verbose_name="name sport")
    def __str__(self):
        return self.name_sport
@python_2_unicode_compatible
class Athlete(models.Model):
    firstname = models.CharField(max_length=30, verbose_name="firsname")
    lastename = models.CharField(max_length=30, verbose_name="lastname")
    phonenumber = models.CharField(max_length=50, verbose_name="phone number")
    namesport = models.ForeignKey('Sport')
    birth_data = models.DateTimeField(verbose_name="date of birthday", null=True,default=None,blank=True)
    visit_first_date = models.DateTimeField(verbose_name=" visit first date",null=True,default=None,blank=True)
    male = models.BooleanField(verbose_name="male")
    famale = models.BooleanField(verbose_name="fmale")
    age = models.IntegerField(verbose_name="age", default=0)
    skill= models.ForeignKey('Skill')
    name_skill = models.CharField(max_length=50,verbose_name="name skill",null=True)
    profil = models.CharField(max_length=300,verbose_name="profil",null=True)
    def __str__(self):
        return self.lastename
@python_2_unicode_compatible
class Skill(models.Model):
    skill_level = models.CharField(max_length=50,verbose_name="skill level")
    def __str__(self):
        return self.skill_level