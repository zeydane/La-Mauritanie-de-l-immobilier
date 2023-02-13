from django.db import models

# Create your models here.

class Action(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Quartier(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class TypedeBien(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# Détails sur les types de biens :

class Terrain(models.Model):
	quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
	action = models.ForeignKey(Action, on_delete=models.CASCADE)
	superficie = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Maison(models.Model):
	superficie = models.CharField(max_length=60)
	prix = models.DecimalField(decimal_places=2, max_digits=4)
	quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
	action = models.ForeignKey(Action, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Appartement(models.Model):
	superficie = models.CharField(max_length=60)
	prix = models.DecimalField(decimal_places=2, max_digits=4)
	quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
	action = models.ForeignKey(Action, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Magazin(models.Model):
	superficie = models.CharField(max_length=60)
	prix = models.DecimalField(decimal_places=2, max_digits=4)
	quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
	action = models.ForeignKey(Action, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class User(models.Model):
	nom = models.CharField(max_length=60)
	prénom = models.CharField(max_length=60)
	mot_de_passe = models.CharField(max_length=60)
	email = models.CharField(max_length=60)

	def __str__(self):
		return self.name
