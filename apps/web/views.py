from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic
from pure_pagination import Paginator

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

        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_projects, 10, request=request)
        all_projects = p.page(page)

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

        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_projects, 10, request=request)
        all_projects = p.page(page)

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

        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_projects, 10, request=request)
        all_projects = p.page(page)

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

        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_projects, 10, request=request)
        all_projects = p.page(page)

        return render(request, "list-pvsystem.html", {
            "all_projects": all_projects
        })


class Echarts1View(generic.ListView):
    '''
    折线图
    '''
    template_name = 'echarts1.html'

    def get(self, request, *args, **kwargs):
        # all_loc = list(siteProfile.objects.order_by('projectNo').values_list('location', flat=True))
        # print(all_loc)
        all_tem = temperature.objects.order_by('projectNo')
        avg_tem = list(all_tem.values_list('avgTemperature', flat=True))
        min_tem = list(all_tem.values_list('minTemperature', flat=True))
        max_tem = list(all_tem.values_list('maxTemperature', flat=True))
        return render(request, 'echarts1.html', locals())


def page_not_found(request, exception):
    return render(request, 'error.html')
