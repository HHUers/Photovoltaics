from django.urls import path, re_path

from . import views

app_name = "web"
urlpatterns = [
    # 首页
    path(
        r'',
        views.IndexView.as_view(),
        name='index'
    ),
]