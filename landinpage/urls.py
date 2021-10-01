from django.urls import path
from . import views
app_name = 'landinpage'

urlpatterns = [

    path('', views.index, name='index'),
    path('<str:title>/portofolio', views.portofolio, name='portofolio')
   
]