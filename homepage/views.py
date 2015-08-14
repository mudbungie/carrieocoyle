from django.shortcuts import render

def index(request):
    # just return the homepage. It's static, so this is simple.
    return render(request, 'homepage/index.html')
