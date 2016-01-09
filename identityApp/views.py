from django.shortcuts import render
from .forms import Mahasiswa

# Create your views here.

def home(request):
    context = {
    }
    templates = "home_v.html"
    return render(request, templates, context)

def login(request):
    form = Mahasiswa()

    context = {
        "form":form,
        "title":title,
    }


    templates = "login_v.html"
    return render(request, templates, context)

def mahasiswa(request):
    context = {
    }
    templates = "identity_temp/mhs_data_v.html"
    return render(request, templates, context)