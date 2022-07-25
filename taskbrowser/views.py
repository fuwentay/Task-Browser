from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "taskbrowser/index.html")

def image(request):
    return render(request, "taskbrowser/image.html")

def advanced(request):
    return render(request, "taskbrowser/advanced.html")