from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Max, Count
from django.views import generic
from pure_pagination import Paginator

from apps.web.models import projectOverview, siteProfile, temperature, PVSystem, projectApplyFor


class IndexView(generic.ListView):
    '''
    主页
    '''
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', locals())


class WelcomeView(generic.ListView):
    '''
    主页
    '''
    template_name = 'welcome.html'

    def get(self, request, *args, **kwargs):
        all_tem = temperature.objects.order_by('projectNo')
        avg_tem = list(all_tem.values_list('avgTemperature', flat=True))
        min_tem = list(all_tem.values_list('minTemperature', flat=True))
        max_tem = list(all_tem.values_list('maxTemperature', flat=True))
        avgSpeed = list(all_tem.values_list('avgSpeed', flat=True))
        avgSpeed = [0 if i is None else i for i in avgSpeed]
        maxSpeed = list(all_tem.values_list('maxSpeed', flat=True))
        maxSpeed = [0 if i is None else i for i in maxSpeed]
        rainyDays = list(all_tem.values_list('rainyDays', flat=True))
        rainyDays = [0 if i is None else i for i in rainyDays]
        print(avgSpeed)
        print(maxSpeed)
        user_post_accept = projectApplyFor.objects.filter(check=1).count()
        user_post_wait = projectApplyFor.objects.filter(check=0).count()
        return render(request, 'welcome.html', locals())


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

    def post(self, request, *args, **kwargs):
        name = request.POST.get('projectNameInput')  # 获取用户输入

        all_projects = projectOverview.objects.filter(projectName__contains=name)  # 模糊查询
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

    def post(self, request, *args, **kwargs):
        name = request.POST.get('projectNameInput')  # 获取用户输入

        projectID = projectOverview.objects.filter(projectName__contains=name).values('projectNo')[0][
            'projectNo']  # 模糊查询
        # print(projectID)

        all_projects = siteProfile.objects.filter(projectNo_id=projectID)

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

    def post(self, request, *args, **kwargs):
        name = request.POST.get('projectNameInput')  # 获取用户输入

        projectID = projectOverview.objects.filter(projectName__contains=name).values('projectNo')[0][
            'projectNo']  # 模糊查询
        # print(projectID)

        all_projects = temperature.objects.filter(projectNo_id=projectID)

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

    def post(self, request, *args, **kwargs):
        name = request.POST.get('projectNameInput')  # 获取用户输入

        projectID = projectOverview.objects.filter(projectName__contains=name).values('projectNo')[0][
            'projectNo']  # 模糊查询
        # print(projectID)

        all_projects = PVSystem.objects.filter(projectNo_id=projectID)

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


class ApplyView(generic.ListView):
    '''
    申请
    '''
    template_name = 'order-add.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'order-add.html', locals())

    def post(self, request, *args, **kwargs):
        new_project = projectApplyFor()
        prn = projectOverview.objects.aggregate(Max('projectNo'))['projectNo__max'] + 1
        cnt = list(projectApplyFor.objects.order_by('id').values_list('id', flat=True))
        new_project.id = max(prn, cnt[-1] + 1)
        new_project.projectName = request.POST.get('projectName', '')
        new_project.projectType = request.POST.get('projectType', '')
        new_project.projectStage = request.POST.get('projectStage', '')
        new_project.projectHost = request.POST.get('projectHost', '')
        new_project.projectHostGroup = request.POST.get('projectHostGroup', '')
        new_project.projectDesign = request.POST.get('projectDesign', '')
        new_project.projectDate = request.POST.get('projectDate', '')
        new_project.status = 0
        new_project.check = 0
        new_project.save()
        flag = True
        return render(request, 'order-add.html', locals())


def page_not_found(request, exception):
    return render(request, 'error.html')
