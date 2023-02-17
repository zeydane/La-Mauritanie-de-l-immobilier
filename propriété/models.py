
from django.db import models


class Property_Type(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Property_Locate(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Profile(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Property(models.Model):
    type = models.ForeignKey(Property_Type, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Property_Locate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.type

class Maison(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Property_Locate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
TERRAIN_TYPES = (
    ('Residential', 'Résidentiel'),
    ('Commercial', 'Commercial'),
    ('Agricultural', 'Agricole'),
    ('Industrial', 'Industriel'),
)
    
class Terrain(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Property_Locate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    area = models.DecimalField(max_digits=10, decimal_places=2)
    terrain_type = models.CharField(max_length=50, choices=TERRAIN_TYPES)
    zoning = models.CharField(max_length=50)
    frontage = models.DecimalField(max_digits=10, decimal_places=2)
    depth = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Appartement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Property_Locate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    garage = models.BooleanField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.PositiveIntegerField()
    balcony = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

