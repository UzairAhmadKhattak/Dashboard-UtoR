from django.urls import path
from .views import home,login_form,signup,logout_form

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',login_form,name='login'),
    path('logout/',logout_form,name='logout'),
    path('signup/',signup,name='signup'),
]