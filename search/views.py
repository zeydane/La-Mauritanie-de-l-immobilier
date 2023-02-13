from django.shortcuts import render
from .models import Terrain, Magazin, TypedeBien, Maison, Appartement, User
from rest_framework import generics, filters
from .serializers import TerrainSerializer, TypedeBienSerializer, MaisonSerializer, AppartementSerializer, UserSerializer, MagazinSerializer
# Create your views here.

class TerrainSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = Terrain.objects.all()
	serializer_class = TerrainSerializer

class MagazinSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = Magazin.objects.all()
	serializer_class = MagazinSerializer

class TypedeBienSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = TypedeBien.objects.all()
	serializer_class = TypedeBienSerializer

class MaisonSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = Maison.objects.all()
	serializer_class = MaisonSerializer

class AppartementSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = Appartement.objects.all()
	serializer_class = AppartementSerializer

class UserSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = User.objects.all()
	serializer_class = UserSerializer