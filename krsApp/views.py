from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from krsApp.models import Mata_Kuliah

# Create your views here.

@login_required(login_url='/login/')
def krs(request, id_mhs):
    title = "KRS Online"
    # matkul = Mata_Kuliah.objects.

    context = {
        "title":title,
    }

    templates = "krs_temp/krs_v.html"
    return render(request, templates, context)
