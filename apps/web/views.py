from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic
from apps.web.models import projectOverview, siteProfile, temperature, PVSystem


class IndexView(generic.ListView):
    '''
    主页
    '''
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', locals())


class ProjectsView(generic.ListView):
    '''
    项目概述
    '''
    template_name = 'list-project.html'

    def get(self, request, *args, **kwargs):
        all_projects = projectOverview.objects.all()
        return render(request, "list-project.html", {
            "all_projects": all_projects
        })


class SitesView(generic.ListView):
    '''
    厂址概述
    '''
    template_name = 'list-site.html'

    def get(self, request, *args, **kwargs):
        all_projects = siteProfile.objects.all()
        return render(request, "list-site.html", {
            "all_projects": all_projects
        })


class TemperatureView(generic.ListView):
    '''
    主要气象特征要素
    '''
    template_name = 'list-temperature.html'

    def get(self, request, *args, **kwargs):
        all_projects = temperature.objects.all()
        return render(request, "list-temperature.html", {
            "all_projects": all_projects
        })

class PvsystemView(generic.ListView):
    '''
    光伏发电系统及发电量
    '''
    template_name = 'list-pvsystem.html'

    def get(self, request, *args, **kwargs):
        all_projects = PVSystem.objects.all()
        return render(request, "list-pvsystem.html", {
            "all_projects": all_projects
        })

def page_not_found(request, exception):
    return render(request, 'error.html')
