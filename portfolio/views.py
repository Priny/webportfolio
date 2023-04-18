from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from portfolio.models import Contact
from django.contrib import messages




# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def workexperience(request):
    return render(request, 'workexperience.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def project(request):
    return render(request, 'project.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def aboutme(request):
    return render(request, 'aboutme.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        emailAddress = request.POST.get('emailAddress')
        message = request.POST.get('message')
        cont = Contact(name=name, emailAddress=emailAddress, message=message)
        cont.save()
        messages.success(request, "Thank you for the feedback!")

    return render(request, 'contact.html')
