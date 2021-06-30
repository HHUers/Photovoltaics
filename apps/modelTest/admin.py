from django.contrib import admin
from modelTest.models import *


class projectOverviewAdmin(admin.ModelAdmin):
    list_display=['projectNo', 'projectName', 'projectType', 'projectStage', 'projectDesign', 'projectDate']
    search_fields=['projectNo', 'projectName']


admin.site.register(projectOverview, projectOverviewAdmin)
admin.site.register(siteProfile)
admin.site.register(temperature)


# Register your models here.
