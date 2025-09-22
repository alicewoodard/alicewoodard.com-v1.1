from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'Website/html/index.html')
