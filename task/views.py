
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Athlete, Sport, Skill,pageview
from .forms import form_athlete
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.exceptions import ValidationError
import logging


class IndexView(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = 'latest_Athlete_list'

    def get_queryset(self):
        return  Athlete.objects.order_by('firstname')[:100]
#**************************************************************************



@login_required(login_url='/admin/login/')
#reporting
def Testview(request):
    template_name = 'task/test.html'
    data = Athlete.objects.order_by('firstname')[:100]
    if request.method == 'GET' and request.GET.get("types"):
        types=request.GET.get("types")
        val=request.GET.get("val")

        if(types =="namesport" and val==val):
            sport=Sport.objects.values_list('id').filter(name_sport=val)
            data=Athlete.objects.filter(namesport=sport)
            #return HttpResponse(data)
        elif(types == "age" and val==val):
             data = Athlete.objects.filter(age=val)
        elif (types =="skill"  and val == val):
             skill = Skill.objects.values_list('id').filter(skill_level=val)
             data = Athlete.objects.filter(skill=skill)
        elif (types =="visit_first_date" and val ==val):
             data = Athlete.objects.filter(visit_first_date=val)


    return render(request,template_name,context={"data":data})
#***************************************************************************************
def bootstrap(request):
    return render(request,'task/bootstrap.html')


#*******************************************************************


@login_required(login_url='/admin/login/')
def athlete(request):
    request.user.is_authenticated
    form=form_athlete()
    return render(request,'task/create_athlete.html',{'form':form})
@login_required(login_url='/accounts/login/')
def my_view(request):
    pass
#**********************************************************************************
def boot1(request):
    return render(request, 'task/boot.html')
#*******************************************************
#@login_required(login_url='/admin/login/')
def home(request):
    contact_list = Athlete.objects.all()
    paginator = Paginator(contact_list,3)
    page = request.GET.get('page',1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    if(pageview.objects.count()<=0):
        x=pageview.objects.create()
        x.save()
    else:
        x=pageview.objects.all()[0]
        x.hits=x.hits+1
        x.save()


    return render(request, 'task/home.html', context={'page':page ,'contacts': contacts,'page':x.hits})
#******************************************************************************
def test(request):
    return render(request, 'task/test.html')
def pagination(request):
    return render(request, 'task/pagination.html')
def main(request):
    return render(request,'task/main.html',context=None)
def show(request):
    return render(request,'task/show.html')
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def index(request):
    return render(request,'task/index.html')
def jquery(request):
    return render(request,'task/jquery.html')
#*******************************************************************
@login_required(login_url='/admin/login/')
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
            #phonenumber = self.cleaned_data['phonenumber']
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



            #firstname=form.cleaned_data['firstname']
            '''
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
            #'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            #messages.success(request, 'Form submission successful')
            messages.success(request, "فرم با موفقیت ذخیره شد")
            logger = logging.getLogger('name')
            hdlr = logging.FileHandler('task.txt')
            formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s')
            hdlr.setFormatter(formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.INFO)
            logger.info('insert1 in system')
            #logger=logging.getLogger('rasool')

            #logging.info("%s instance %s (pk %s) updated" )

           # return HttpResponse("فرم با موفقیت ذخیره شد")
        else:
            return render(request,'task/create_athlete.html', {'form': form})
    else:
        form = form_athlete()

    return render(request, 'task/create_athlete.html', {'form': form})
@login_required(login_url='/admin/login/')
def delete_item(request):
    if request.method == "POST":
        form =form_athlete(request.POST)
        inventory=Athlete.objects.all()
        item_id = int(request.POST.get('item_id'))
        item = Athlete.objects.get(id=item_id)
        item.delete()
        logger = logging.getLogger('name')
        hdlr = logging.FileHandler('task.txt')
        formatter = logging.Formatter('%(asctime)s [%(name)s:%(lineno)s]  %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
        logger.info('delete in system')
        return render(request, 'task/index.html', {
            'form': form, 'inventory': inventory})

    return HttpResponseRedirect("task/index.html")
#***********************************************************************
def server_update(request, pk):
    #model=Athlete
        alert = "apdate is succes"
        instance = get_object_or_404(Athlete, id=pk)
        form = form_athlete(request.POST or None, instance=instance)
        if request.method == 'POST':
            logger = logging.getLogger('name')
            hdlr = logging.FileHandler('task.txt')
            formatter = logging.Formatter('%(asctime)s [%(name)s:%(lineno)s]  %(message)s')
            hdlr.setFormatter(formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.INFO)
            logger.info('update2 in system')
            form.save()




        #return render(request, 'update.html', {'form': form, 'alert': alert})
        return render(request, 'task/update_athlete.html', {'form': form,'alert':alert})



#def logs(user_id,action):







