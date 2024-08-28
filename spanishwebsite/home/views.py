from django.shortcuts import render

# Create your views here.
def home(result): 
    return render(result, "home/index.html")