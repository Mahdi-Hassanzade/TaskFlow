from django.urls import path
from .views import *

urlpatterns = [
    path('',Main.as_view()),
    path('add/', Add.as_view(), name='Add'),
    path('update/<int:id>/', Update.as_view(), name='update'),
    path('delete/<int:id>/', Delete.as_view(), name='delete'),
    path('complete/<int:id>/',Complete.as_view(),name='complete')
]