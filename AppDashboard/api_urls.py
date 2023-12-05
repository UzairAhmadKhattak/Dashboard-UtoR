from django.urls import path
from .views import create_app,update_app,delete_app,change_plan

urlpatterns = [
    path('create_app',create_app,name='create_app'),
    path('update_app/<str:pk>',update_app,name='update_app'),
    path('delete_app/<str:pk>',delete_app,name='delete_app'),
    path('change_plan',change_plan,name='change_plan'),
]