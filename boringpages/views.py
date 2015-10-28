from django.shortcuts import render
from boringpages.models import TextPage

def home(request):
    # splash screen with a picture
    return render(request, 'boringpages/home.html')

def textPage(request, pageName):
    # splash screen with a text blurb
    pageContent = TextPage.objects.filter(title=pageName)[0]
    return render(request, 'boringpages/textpage.html', {'pageContent':pageContent})

def about(request):
    return textPage(request, 'About')

def contact(request):
    return textPage(request, 'Contact')

