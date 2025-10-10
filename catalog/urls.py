from django.urls import path
from . import views  # make sure this line is here and correct

urlpatterns = [
    path('', views.index, name='index'),
]

