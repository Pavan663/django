from django.urls import path

from django.conf.urls import url

from courses import views as courses_views

urlpatterns = [
    path('',courses_views.index, name='index'),
]