from rest_framework import serializers

from .models import Action, Quartier, Terrain, Magazin, TypedeBien, Maison, Appartement, User

class ActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Action
		fields = "__all__"

class QuartierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quartier
		fields = "__all__"

class TerrainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Terrain
		fields = "__all__"

class MagazinSerializer(serializers.ModelSerializer):
	class Meta:
		model = Magazin
		fields = "__all__"

class TypedeBienSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypedeBien
		fields = "__all__"

class MaisonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maison
		fields = "__all__"

class AppartementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appartement
		fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"