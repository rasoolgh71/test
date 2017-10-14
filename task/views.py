from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("hi rasool ,hi db")
# Create your views here.

'''
def countries_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('countries')
            # do something with your results
    else:
        form = CountryForm

    return render_to_response('render_country.html', {'form':form },
        context_instance=RequestContext(request))'''
