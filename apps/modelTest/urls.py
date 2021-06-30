from django.contrib import admin
from django.urls import path, include
from modelTest.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_projectOverview/', list_projectOverview),

]
