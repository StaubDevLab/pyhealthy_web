from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),

]
