from django.http import Http404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Athlete
from .forms import form_athlete
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
class IndexView(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = 'latest_Athlete_list'
    def get_queryset(self):
        return  Athlete.objects.order_by('firstname')[:10]
class DetailView(generic.DetailView):
    model = Athlete
    template_name = 'task/detail.html'

'''def detail(request, question_id):
    question = get_object_or_404(Athlete,pk=firtname)
    return render(request, 'task/detail.html', {'question': question})'''

class ResultsView(generic.DetailView):
    model = Athlete
    template_name = 'task/results.html'

'''def results(request, question_id):
    question = get_object_or_404(Athlete, pk=firtname)
    return render(request, 'task/detail.html', {'question': question})'''
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
            firstname = request.POST.get('firsname', '')
            lastename = request.POST.get('lastename','')
            phonenumber =request.POST.get('phonenumber','')

            HttpResponse(phonenumber)
            namespor =request.POST.get('namesport','')
            birth_data=request.POST.get('birth_data','')
            visit_first_date=request.POST.get('visit_first_data','')
            male=request.POST.get('male','')
            famale=request.POST.get('famel','')
            age=request.POST.get('age','')
            skill=request.POST.get('skill','')
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
            new_athlete = Athlete(firstname=firstname,lastename=lastename,phonenumber=phonenumber,namespor=namespor,
                                birth_data=birth_data,visit_first_datev=visit_first_date,
                                male=male,famale=famale,age=age,skill=skill,name_skill=name_skill,profil=profil)
            #print(firstname)
            new_athlete.save()
            #return HttpResponseRedirect("thank")
        else:
            return render(request,'task/create_athlete.html', {'form':form})
    else:
        form = form_athlete()

    return render(request, 'task/create_athlete.html', {'form': form})
