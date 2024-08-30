from django.db import models





class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Contacts(models.Model):
    platform = models.CharField(max_length=100)  
    url = models.CharField(max_length=200)         

    def __str__(self):
        return f"{self.platform} - {self.url}"


class House(models.Model):
    title = models.CharField(max_length=255)
    model_3d = models.FileField(blank=True, upload_to='3d_models/')
    description = models.TextField()
    total_area = models.FloatField()
    effective_area = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    blueprint = models.FileField(upload_to='blueprints/')

class ExteriorPhoto(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='exterior_photos')
    photo = models.ImageField(upload_to='exterior_photos/')

class InteriorPhoto(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='interior_photos')
    photo = models.ImageField(upload_to='interior_photos/')

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)  
    area = models.FloatField()