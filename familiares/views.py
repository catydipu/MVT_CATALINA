from django.shortcuts import render
from django.http import HttpResponse


def lista_familiares(request):
    contex = {
        'nombre_1': 'Cristina',
        'edad_1':64,
        'carnet_de_conducir_1': True,
        'nombre_2': 'Constanza',
        'edad_2':25,
        'carnet_de_conducir_2': False,
        'nombre_3': 'Catalina',
        'edad':29,
        'carnet_de_conducir_3': False
    }
    return render(request, 'familiares.html', context=contex )