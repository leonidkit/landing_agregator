from django.urls import path, include
from smartwatch import views

urlpatterns = [
    path('', views.index, name='index'),
]
