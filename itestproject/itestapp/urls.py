from django.urls import path

from itestapp import views

urlpatterns=[
    path('',views.person_detail,name='log'),
    path('logdata', views.logdata_fun),
]