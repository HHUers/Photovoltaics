
from .models import *
from django.shortcuts import render


def list_projectOverview(request):
    projectOverview_list = projectOverview.objects.all()
    return render(request, 'testmodel/test.html', {'projectOverview_list': projectOverview_list})


