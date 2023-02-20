from django.urls import path
from . import views

from .views import test, getdata

urlpatterns = [
    path('properties/', views.PropertySearchAPI.as_view()),
    path('maison/', views.MaisonSearchAPI.as_view()),
    path('appartement/', views.AppartementSearchAPI.as_view()),
    path('terrain/', views.TerrainSearchAPI.as_view()),
    path('person/', getdata),
    path('test/', test)

]