from django.shortcuts import render
from information.models import Family


def create_family(request):
    information_family=Family.objects.create(name="Mariano",age=35,creation_date="2022-12-09")
    context={ 
        "information_family":information_family
    }
    return render(request,"information_family.html",context=context)

def list_family(request):
    relatives=Family.objects.all
    context={
        "relatives":relatives
    }
    return render (request,"relatives_list.html",context=context)

