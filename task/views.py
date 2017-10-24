from django.http import Http404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Athlete, Sport, Skill
from .forms import form_athlete
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
class IndexView(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = 'latest_Athlete_list'
    def get_queryset(self):
        return  Athlete.objects.order_by('firstname')[:100]

class Testview(generic.ListView):
    template_name = 'task/test.html'
    context_object_name = 'athlete_list'
    def get_queryset(self):
        return Athlete.objects.order_by('firstname')[:200]


def athlete(request):
        return render(request,'task/create_athlete.html')
def boot1(request):
    return render(request, 'task/boot.html')
def home(request):
    return render(request, 'task/home.html')
def test(request):
    return render(request, 'task/test.html')
def main(request):
    return render(request,'task/main.html',context=None)
def show(request):
    return render(request,'task/show.html')
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def index(request):
    return render(request,'task/index.html')

def add(request):
    if request.method == 'POST':
        form=form_athlete(request.POST)
        if form.is_valid():
            #soss = request.POST.get('soss', '')
            firstname = request.POST.get('firstname', '')
            lastename = request.POST.get('lastename','')
            #Post(firstname=firstname, lastename=lastename).save()
            #Athlete(firstname=firstname, lastename=lastename).save()

            phonenumber =request.POST.get('phonenumber','')
            #HttpResponse(phonenumber)
            sport_id=request.POST.get('namesport','')
            namesport =Sport.objects.get(id=sport_id)
            birth_data =request.POST.get('birth_data','')
            visit_first_date =request.POST.get('visit_first_date','')
            male=request.POST.get('male','')
            famale=request.POST.get('famel','')
            age=request.POST.get('age','')
            skill_id=request.POST.get('skill','')
            skill=Skill.objects.get(id=skill_id)
            name_skill=request.POST.get('name_skill','')
            profil=request.POST.get('profil','')
            '''
            firstname=form.cleaned_data['firstname']
            lastename=form.cleaned_data['lastname']
            phonenumber=form.cleaned_data['phonenumber']
            namespor =form.cleaned_data['nemesport']
            birth_data=form.cleaned_data['birth_data']
            visit_first_date =form.cleaned_data['visit_first_data']
            male= form.cleaned_data['male']
            famale=form.cleaned_data['famale']
            age=form.cleaned_data['age']
            skill=form.cleaned_data['skill']
            name_skill=form.cleaned_data['name_skill']
            profil=form.cleaned_data['profil']'''
            new_athlete = Athlete(firstname=firstname,lastename=lastename,phonenumber=phonenumber,namesport=namesport,
                                birth_data=birth_data,visit_first_date=visit_first_date,
                                male=male,famale=famale,age=age,skill=skill,name_skill=name_skill,profil=profil)
            #print(firstname)
            new_athlete.save()
            #messages.success(request, 'Form submission successful')
            messages.success(request, "Huge success!")
            #return HttpResponse("فرم با موفقیت ذخیره شد")
        else:
            return render(request,'task/create_athlete.html', {'form': form})
    else:
        form = form_athlete()

    return render(request, 'task/create_athlete.html', {'form': form})
def delete_item(request):
    #context_object_name = 'latest_Athlete_list'
    if request.method == "POST":
        form =form_athlete(request.POST)
        inventory=Athlete.objects.all()
        item_id = int(request.POST.get('item_id'))
        item = Athlete.objects.get(id=item_id)
        item.delete()
        #athlete.refresh_from_db()
        return render(request,'index.html', {
            'form': form, 'inventory': inventory})
    return HttpResponseRedirect("/form_url/?success=1")
def update_item(request):
    if request.method == "POST":
        form=form_athlete(request.POST)
        #inventory=Athlete.objects.get(firstname= firstname).update(field=value)
        #Athlete.objects.filter().update(active=True)
        Athlete.objects.all().update()
        #save(update_fields=[firstname,lastname])
        #item_id=int(request.POST.get('item_id'))
        #item=Athlete.objects.get(id=item_id)
        #item.update()
        return render(request,'index.html',{'form':form})



