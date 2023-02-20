from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, filters, viewsets
from .serializers import PropertySerializer, PersonSerializer
from .models import Property, Terrain, Maison, Appartement, Persons
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

@api_view(['GET'])
@permission_classes([AllowAny])
def test(request):
	if request.method == 'GET':
		print(request.query_params)
		#get_value = request.query_params['id']
		message = {'name':'Seydou', 'id':'4'}
		return Response(message)
	
class PersonView(viewsets.ModelViewSet):
	serializer_class = PersonSerializer

	def get_queryset(self):
		person_data = Persons.objects.all()
		return person_data
	
@api_view(['GET'])
@permission_classes([AllowAny])
def getdata(request):
	person_data = Persons.objects.all()
	person_serialized = PersonSerializer(person_data, many = True)
	return Response(person_serialized.data)

