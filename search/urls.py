from django.urls import path

from . import views

urlpatterns = [
    path('terrain/', views.TerrainSearchAPI.as_view()),
    path('typedebien/', views.TypedeBienSearchAPI.as_view()),
    path('maison/', views.MaisonSearchAPI.as_view()),
    path('magazin/', views.MagazinSearchAPI.as_view()),
    path('appartement/', views.AppartementSearchAPI.as_view()),
    path('user/', views.UserSearchAPI.as_view()),
]
