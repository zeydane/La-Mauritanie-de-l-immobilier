from django.contrib import admin

from .models import Action, Quartier, Terrain, Magazin, Maison, Appartement, TypedeBien, User

# Register your models here.
admin.site.register(Action)
admin.site.register(Quartier)
admin.site.register(TypedeBien)

admin.site.register(Maison)
admin.site.register(Appartement)
admin.site.register(Terrain)
admin.site.register(Magazin)

admin.site.register(User)
# admin.site.register(SundayChamber)
# admin.site.register(MondayChamber)
# admin.site.register(TuesdayChamber)
# admin.site.register(WednesdayChamber)
# admin.site.register(ThursdayChamber)
# admin.site.register(FridayChamber)
# admin.site.register(SaturdayChamber)
# admin.site.register(Appointment)