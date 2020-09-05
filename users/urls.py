from django.urls import path
from . import views

urlpatterns = [
    path('ajax_logout', views.ajax_logout, name='ajax_logout'),
    path('ajax_login', views.ajax_login, name='ajax_login'),
    path('signup', views.signup, name='signup'),

]
