from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def services(request):

    return render(request, 'service.html')

def appointment(request):

    return render(request, 'appointment.html')

def features(request):

    return render(request, 'feature.html')

def blog(request):

    return render(request, 'blog.html')

def team(request):

    return render(request, 'team.html')

def testmonial(request):

    return render(request, 'testmonial.html')

def contact(request):

    return render(request, 'contact.html')