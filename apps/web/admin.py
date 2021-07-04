from django.contrib import admin
from apps.web.models import *


# 日期  可以选择加或者不加
# from django.utils import timezone



# class projectApplyForAdmin(admin.ModelAdmin):
#     """
#         *MySQL数据库moderate表：id, 名字, 内容，是否通过, 是否已审核
#         'id', 'name', 'incident', 'status', 'check'
#     """
#     # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('name', 'incident', 'status',)
#     # list_per_page设置每页显示多少条记录，默认是10条
#     list_per_page = 10
#     # list_filter过滤指定的字段
#     list_filter = ('name',)




class projectOverviewAdmin(admin.ModelAdmin):
    list_display = ['projectNo', 'projectName', 'projectType', 'projectStage', 'projectDesign', 'projectDate']
    search_fields = ['projectNo', 'projectName']
    list_filter = ['projectNo', 'projectName']


admin.site.register(projectOverview, projectOverviewAdmin)


class siteProfileAdmin(admin.ModelAdmin):
    list_display = ['projectNo', 'location', 'capacity', 'area', 'altitude', 'longtitude', 'latitude', 'radiationMJ',
                    'radiationkwh', 'dipAngle']
    search_fields = ['projectNo', 'location', 'longtitude', 'latitude']
    list_filter = ['projectNo', 'location', 'longtitude', 'latitude']


admin.site.register(siteProfile, siteProfileAdmin)


class temperatureAdmin(admin.ModelAdmin):
    list_display = ['projectNo', 'avgTemperature', 'maxTemperature', 'minTemperature', 'avgMonthTemperature',
                    'breakingGroundDepth',
                    'avgSpeed', 'maxSpeed', 'rainyDays', 'pollutionLevel']
    search_fields = ['projectNo']
    list_filter = ['projectNo']


admin.site.register(temperature, temperatureAdmin)


class PVSystemAdmin(admin.ModelAdmin):
    list_display = ['projectNo', 'component', 'installedAngle', 'plan', 'inverter',
                    'capacityRatio', 'inclinedRadiation', 'systemEffience', 'avgElectricity',
                    'avgHours', 'firstYearHours', 'firstConnect', 'fullConnect']
    search_fields = ['projectNo']
    list_filter = ['projectNo']


admin.site.register(PVSystem, PVSystemAdmin)


class projectApplyForAdmin(admin.ModelAdmin):
    list_display = ['projectName', 'projectType', 'projectStage', 'projectDesign', 'projectDate', 'status', 'check']

    search_fields = ['projectName']
    list_filter = ['projectName', ]
    list_per_page = 10
    # 修改admin页面actions的信息
    actions = ['mak_pub', 'mak_pub1']

    # 判断通过的
    def mak_pub(self, request, queryset):
        # 获取当前用户的名字
        us = request.user
        # 打印通过的数据
        for i in queryset.filter():
            # print(i.id)
            # 创建str，如果要加时间的话，就加上下面的代码
            # str = '{} {}更改了Moderate表的id为{}的信息：已通过，审核成功！'.format(timezone.now(), us, i.id)
            str1 = '{}更改了Moderate表的id为{}的信息：已通过，审核成功！'.format(us, i.id)
            # 插入数据到Log表中
            projectApplyForLog.objects.create(record=str1)

        # 更新状态和审核
        rows_upb = queryset.update(status="1", check="1")
        # 如果获取的数是1,则执行下面代码
        if rows_upb == 1:
            message_bit = "1个申请"
        else:
            message_bit = "%s 个申请" % rows_upb
        # 通过多少的数据，显示到admin页面上
        self.message_user(request, "%s 已经通过." % message_bit)
        ZW0 = projectApplyFor.objects.values_list('id', flat=True).distinct()
        ZW1 = projectApplyFor.objects.values_list('projectName', flat=True).distinct()
        ZW2 = projectApplyFor.objects.values_list('projectType', flat=True).distinct()
        ZW3 = projectApplyFor.objects.values_list('projectStage', flat=True).distinct()
        ZW4 = projectApplyFor.objects.values_list('projectDesign', flat=True).distinct()
        ZW5 = projectApplyFor.objects.values_list('projectDate', flat=True).distinct()
        print(ZW0[0],ZW1[0],ZW2[0])
        u1 = projectOverview(projectNo=ZW0[0], projectName=ZW1[0], projectType=ZW2[0], projectStage=ZW3[0],
                             projectDesign=ZW4[0], projectDate=ZW5[0])

        u1.save()
        u1.save()

    # 更改Action的内容为通过
    mak_pub.short_description = "通过"

    # 判断未通过的
    def mak_pub1(self, request, queryset):
        # 获取当前的用户
        us = request.user
        # 打印未通过的数据
        for i in queryset.filter():
            print(i)
            # 创建str
            str1 = '{}更改了Moderate表的id为{}的信息：未通过，审核成功！'.format(us, i.id)
            # 插入数据到Log表中
            projectApplyForLog.objects.create(record=str1)
        # 更新状态和审核
        rows_upb = queryset.update(status="0", check="1")
        # 如果获取的数是1,则执行下面代码
        if rows_upb == 1:
            message_bit = "1个申请"
        else:
            message_bit = "%s 个申请" % rows_upb
        # 通过多少的数据，显示到admin页面上
        self.message_user(request, "%s 拒绝通过." % message_bit)

    # 更改Action的内容为通过
    mak_pub1.short_description = "未通过"

    # 重写已经审核过的数据，超级管理员不会通过
    def get_queryset(self, request):
        # 获取当前表所有的数据
        qs = super().get_queryset(request)
        # 判断是否未超级管理员，如果是就显示所有(已审核和未审核)的信息，不是就显示未审核的信息
        if request.user.is_superuser:
            return qs
        return qs.filter(check=0)


admin.site.register(projectApplyFor, projectApplyForAdmin)
