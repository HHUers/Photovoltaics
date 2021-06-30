from django.contrib import admin
from apps.web.models import *


class projectOverviewAdmin(admin.ModelAdmin):
    list_display=['projectNo', 'projectName', 'projectType', 'projectStage', 'projectDesign', 'projectDate']
    search_fields=['projectNo', 'projectName']


admin.site.register(projectOverview, projectOverviewAdmin)


class siteProfileAdmin(admin.ModelAdmin):
    list_display=['projectNo', 'location', 'capacity', 'area', 'altitude', 'longtitude', 'latitude', 'radiationMJ', 'radiationkwh', 'dipAngle']
    search_fields=['projectNo', 'location', 'longtitude', 'latitude']


admin.site.register(siteProfile, siteProfileAdmin)


class temperatureAdmin(admin.ModelAdmin):
    list_display=['projectNo', 'avgTemperature', 'maxTemperature', 'minTemperature', 'avgMonthTemperature', 'breakingGroundDepth',
                  'avgSpeed', 'maxSpeed', 'rainyDays', 'pollutionLevel']
    search_fields=['projectNo']


admin.site.register(temperature, temperatureAdmin)
admin.site.register(PVSystem)


