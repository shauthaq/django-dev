from django.urls import path
from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.asset_list, name='list'),  # http://localhost:7000/ でアクセス
]
