from django.shortcuts import render
from django.http import HttpResponse
from.models import Hotel
from.forms import Hotel_form

# Create your views here.

def home(request):
    return render(request=request,template_name='home.html') 



def accomodation(request):
    return render(request=request,template_name='accomodation.html')



def hotelDetails(request):
    if request=="POST":
        Hotelform=Hotel_form(request.POST)
        if Hotelform.is_valid():
            Hotelform.save()
        else:
            massages.error(request,('your data is invalid'))
    Hotelform=Hotel_form()
    return render(request=request,template_name="hotelDetails.html",context={'Hotelform':Hotelform})


def hotellist(request):
    hotel=Hotel.objects.all()
    return render(request=request,template_name="hotellist.html",context={"hotel":hotel})


def form(request):
    if request.method=="POST":
        name=request.POST['name']
        price=request.POST['price']
        location=request.POST['location']
        new_applicant =Applicant(name=name, price=price, location=location)
        new_applicant.save()
    return render( request,'home.html')