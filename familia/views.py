from django.shortcuts import render
from django.http import HttpResponse

from familia.models import Family

# Create your views here.
def create_family(request):
    Family.objects.create (name ='Catalina', age = 29, license = False )
    return HttpResponse('Nuevo Integrante') 

def list_family(request):
    all_family = Family.objects.all()
    context = {
        'family':all_family,
    }
    return render(request, 'list_family.html', context=context)    