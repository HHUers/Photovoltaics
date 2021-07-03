from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    # 首页
    path(
        r'',
        views.IndexView.as_view(),
        name='index'
    ),
    path(
        r'projects/',
        views.ProjectsView.as_view(),
        name='projects'
    ),
    path(
        r'sites/',
        views.SitesView.as_view(),
        name='sites'
    ),
    path(
        r'temperature/',
        views.TemperatureView.as_view(),
        name='temperature'
    ),
    path(
        r'pvsystem/',
        views.PvsystemView.as_view(),
        name='pvsystem'
    ),
    path(
        r'echarts1/',
        views.Echarts1View.as_view(),
        name='echarts1'
    )
]
