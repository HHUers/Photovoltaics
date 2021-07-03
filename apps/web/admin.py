from django.contrib import admin
from apps.web.models import *


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
    list_display = ['projectName', 'projectType', 'projectStage', 'projectDesign', 'projectDate','projectStatus']

    search_fields = ['projectName']
    list_filter = ['projectName']



admin.site.register(projectApplyFor, projectApplyForAdmin)