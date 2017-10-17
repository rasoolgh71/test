from django.http import Http404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Athlete
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
class IndexView(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = 'latest_Athlete_list'
    def get_queryset(self):
        return  Athlete.objects.order_by('-firstname')[:10]
        #return  Athlete.objects.filter('-firstname').order_by('-firstname')
    #latest_Athlete_list = Athlete.objects.order_by('-lastename')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-phonenumber')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-namesport')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-birth_data')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-visit_first_date')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-male')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-famale')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-age')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-skill')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-name_skill')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-profil')[:5]
    #latest_Athlete_list = Athlete.objects.order_by('-skill')[:5]


    #context = {'latest_Athlete_list':latest_Athlete_list

              # }
    #return render(request,'task/index.html',context)
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


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''
from .forms import Athleteform
def showforms(request):
    athltete_form = Athleteform(request.POST or None)
    if athltete_form.is_valid():
        athltete_form.save()
    context = {'form':athltete_form}
    return render('showforms.html', context, context_instance=RequestContext(request))'''
