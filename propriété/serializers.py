from rest_framework.serializers import ModelSerializer
from .models import Persons, Property, Property_Type, Property_Locate, Maison, Terrain, Appartement, Profile


class Property_TypeSerializer(ModelSerializer):
    class Meta:
        model = Property_Type
        fields = '__all__'

class Property_LocateSerializer(ModelSerializer):
    class Meta:
        model = Property_Locate
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class MaisonSerializer(ModelSerializer):
    class Meta:
        model = Maison
        fields = '__all__'
    
class TerrainSerializer(ModelSerializer):
    class Meta:
        model = Terrain
        fields = '__all__'

class AppartementSerializer(ModelSerializer):
    class Meta:
        model = Appartement
        fields = '__all__'

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Persons 
        fields = ['idvalue', 'first_name', 'last_name', 'email', 'avatar']
