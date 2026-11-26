from django.urls import path
from .views import *

urlpatterns=[
    path('verify/',verify,name='verify'),
    path('login/',auth_login,name='login'),
    path('logout/',auth_logout,name='logout')
]