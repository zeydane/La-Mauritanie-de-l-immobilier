from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from .serializers import PropertySerializer
from .models import Property, Terrain, Maison, Appartement
from .serializers import TerrainSerializer, TerrainSerializer, MaisonSerializer, AppartementSerializer

class PropertySearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['title',]
	queryset = Property.objects.all()
	serializer_class = PropertySerializer

class TerrainSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['title',]
	queryset = Terrain.objects.all()
	serializer_class = TerrainSerializer
        
class MaisonSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['title',]
	queryset = Maison.objects.all()
	serializer_class = MaisonSerializer
	
class AppartementSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['title',]
	queryset = Appartement.objects.all()
	serializer_class = AppartementSerializer



