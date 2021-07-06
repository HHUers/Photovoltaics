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
        # print(avgSpeed)
        # print(maxSpeed)
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
        projectName = request.POST.get('projectNameInput')  # 获取用户输入项目名称
        projectType = request.POST.get('projectType')  # 获取用户输入项目类型
        projectStage= request.POST.get('projectStage')  # 获取用户输入项目阶段
        projectDesign= request.POST.get('projectDesign')  # 获取用户输入项目阶段

        dic = dict()  # 定一个字典用于保存前端发送过来的查询条件
        if projectName:
            dic['projectName__contains'] = projectName
        if projectType:
            dic['projectType__contains'] = projectType
        if projectStage:
            dic['projectStage__contains'] = projectStage
        if projectDesign:
            dic['projectDesign__contains'] = projectDesign

        all_projects = projectOverview.objects.filter(**dic)  # 获得查询结果

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
        projectName = request.POST.get('projectNameInput')  # 获取用户输入项目名称
        print(projectName)
        location = request.POST.get('location')
        capacity= request.POST.get('capacity')
        area= request.POST.get('area')
        radiationMJ=request.POST.get('radiationMJ')

        dic = dict()  # 定一个字典用于保存前端发送过来的查询条件
        if projectName:
            dic['projectNo_id'] = projectOverview.objects.filter(projectName__contains=projectName).values('projectNo')[0][
                'projectNo']
        if location:
            dic['location__contains'] = location
        if capacity:
            dic['capacity__gt'] = capacity
        if area:
            dic['area__gt'] = area
        if radiationMJ:
            dic['radiationMJ__gt'] = radiationMJ
        print(dic)
        all_projects = siteProfile.objects.filter(**dic)  # 获得查询结果

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
        projectName = request.POST.get('projectNameInput')  # 获取用户输入项目名称
        print(projectName)
        avgTemperature = request.POST.get('avgTemperature')
        breakingGroundDepth= request.POST.get('breakingGroundDepth')
        avgSpeed= request.POST.get('avgSpeed')

        dic = dict()  # 定一个字典用于保存前端发送过来的查询条件
        if projectName:
            dic['projectNo_id'] = projectOverview.objects.filter(projectName__contains=projectName).values('projectNo')[0][
                'projectNo']
        if avgTemperature:
            dic['avgTemperature__gt'] = avgTemperature
        if breakingGroundDepth:
            dic['breakingGroundDepth__gt'] = breakingGroundDepth
        if avgSpeed:
            dic['avgSpeed__gt'] = avgSpeed

        print(dic)
        all_projects = temperature.objects.filter(**dic)  # 获得查询结果

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
        projectName = request.POST.get('projectNameInput')  # 获取用户输入项目名称
        print(projectName)
        component = request.POST.get('component')
        installedAngle= request.POST.get('installedAngle')
        avgElectricity= request.POST.get('avgElectricity')

        dic = dict()  # 定一个字典用于保存前端发送过来的查询条件
        if projectName:
            dic['projectNo_id'] = projectOverview.objects.filter(projectName__contains=projectName).values('projectNo')[0][
                'projectNo']
        if component:
            dic['component__gt'] = component
        if installedAngle:
            dic['installedAngle__gt'] = installedAngle
        if avgElectricity:
            dic['avgElectricity__gt'] = avgElectricity

        print(dic)
        all_projects = PVSystem.objects.filter(**dic)  # 获得查询结果

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
        if len(cnt) == 0:
            id = prn
        else:
            id = max(prn, cnt[-1] + 1)
        # print(id)
        new_project.id = id
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
