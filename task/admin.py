from django.contrib import admin
from .models import Athlete, Sport, Sex, Skill

# Register your models here.
admin.site.register(Athlete)
admin.site.register(Sport)
admin.site.register(Sex)
admin.site.register(Skill)
#admin.site.register(Supervisor)
