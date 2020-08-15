from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("Hello World")
    return render(request, 'home.html', {})
   
def contact_view( *args, **kwargs):
    return HttpResponse("Contac Page")

def about_view( *args, **kwargs):
    return HttpResponse("About Page")