
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Athlete, Sport, Skill
from .forms import form_athlete
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.core.urlresolvers import reverse
#from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
class IndexView(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = 'latest_Athlete_list'
    def get_queryset(self):
        return  Athlete.objects.order_by('firstname')[:100]
# class Developer_detail(DeleteView):
#     model = Athlete
#     template_name = 'task/index.html'
#     def get_context_data(self, **kwargs):
#         context=super(Developer_detail,self).get_context_data(**kwargs)
#         task_dev=Athlete.objects.filter(0)

class Testview(generic.ListView):
    template_name = 'task/test.html'
    context_object_name = 'athlete_list'
    def get_queryset(self):
        return Athlete.objects.order_by('firstname')[:200]


def athlete(request):
    form=form_athlete()
    return render(request,'task/create_athlete.html',{'form':form})
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
            #messages.success(request, 'Form submission successful')
            messages.success(request, "فرم با موفقیت ذخیره شد")
           # return HttpResponse("فرم با موفقیت ذخیره شد")
        else:
            return render(request,'task/create_athlete.html', {'form': form})
    else:
        form = form_athlete()

    return render(request, 'task/create_athlete.html', {'form': form})
def delete_item(request):
    if request.method == "POST":
        form =form_athlete(request.POST)
        inventory=Athlete.objects.all()
        item_id = int(request.POST.get('item_id'))
        item = Athlete.objects.get(id=item_id)
        item.delete()
        return render(request, 'index.html', {
            'form': form, 'inventory': inventory})
    return HttpResponseRedirect("/form_url/?success=1")
# class Form_task_time(form_athlete):
#     class Meta:
#         model =Athlete
#         fields = ['firstname','lastename','phonenumber',' namesport','birth_data',' visit_first_date',
#                   'male','famale','age',' skill','name_skill','profil']
# class UpdateViewCustom(UpdateView):
#     template_name = 'task/update_athlete.html'
#     url_name = ""
# #     #form_class = Form_task_time
# #     #success_url = 'public_empty'
#     def get_success_url(self):
#         return reverse(self.success_url)
#     def get_context_data(self, **kwargs):
#         context=super(UpdateViewCustom,self).get_context_data(self,**kwargs)
#         model_name = self.model._meta.verbose_name.title()
#         context['model_name'] = model_name
#         context['url_name'] = self.url_name
#         return context
#class form(forms.ModelForm):
#   class Meta:
        #model = User
 #      fields = [...] 'lastename', 'phonenumber']
def server_update(request, pk):
    #model=Athlete
        alert = "";
        instance = get_object_or_404(Athlete, id=pk)
        form = form_athlete(request.POST or None, instance=instance)
        if request.method == 'POST':
            form.save()
        #return render(request, 'update.html', {'form': form, 'alert': alert})
        return render(request, 'task/update_athlete.html', {'form': form})


    #server = Athlete.objects.get(id=pk)
    #server = request.session.get(id=pk)
    #form = form_athlete(request.POST or None)
    #server = Athlete.objects.filter(id=pk).update()
    #if form.is_valid():
     #   form.save()
    #data = request.POST.get('firstname')
    #print(data)
    #server = get_object_or_404(Athlete, id=pk)
    #instance = get_object_or_404(Athlete, id=pk)
    #form = form_athlete(request.POST or None, instance=instance)
    #if form.is_valid():
     #   form.save()
    #
    #form = form_athlete(initial={'firstname':server.firstname,'lastename':server.lastename,'phonenumber':server.phonenumber,
     #                            'namesport':server.namesport, 'birth_data':server.birth_data,
      #                           ' visit_first_date':server. visit_first_date,
       #                          'male':server.male,'famale':server.famale,'age':server.age,'skill':server.skill,
        #                         'name_skill':server.name_skill,'profil':server.profil
         #                        })
    #f = form(request)
    #new_article = f.save()
    #server = Athlete.objects.filter(id=pk).update()

    #p.__dict__.update(form)
    #p.save()
    #form_athlete.save()
    #eturn redirect(object)
    #j=form.save()
    #form.save()
    #server=Athlete.objects.filter(id=pk).update({"firstname":form.firstname})
    #form = form_athlete(server)

    #if request.method == "POST":
     #   form = form_athlete(request.POST)
      #  if form.is_valid():
       #     new_athlete =form
            # print(firstname)
        #    new_athlete.save()
            #form.save()
    #return redirect(server)






