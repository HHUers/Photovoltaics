from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views import generic


class IndexView(generic.ListView):
    '''
    主页
    '''

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', locals())
