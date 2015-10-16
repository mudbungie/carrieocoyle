from django.shortcuts import render

def home(request):
    # splash screen with no content
    return render(request, 'boringpages/home.html')

def about(request):
    # splash screen with a text blurb
    return render(request, 'boringpages/about.html')

def contact(request):
    # splash screen with a text blurb
    return render(request, 'boringpages/contact.html')
