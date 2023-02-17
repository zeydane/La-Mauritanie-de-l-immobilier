from django.contrib import admin

from .models import Property, Property_Locate, Property_Type, Maison, Terrain, Appartement

admin.site.register(Property_Type)
admin.site.register(Property_Locate)
admin.site.register(Property)
admin.site.register(Maison)
admin.site.register(Terrain)
admin.site.register(Appartement)



