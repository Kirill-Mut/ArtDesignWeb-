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
    main_photo = models.ImageField(upload_to='main_photos/', default='Main\static\images\tq__iesr2jwby-x1cp-1500h.png')

class InternalPhoto(models.Model):
    filename = models.ImageField(upload_to='internal_photos/')
    house = models.ForeignKey(House, related_name='internal_photos', on_delete=models.CASCADE)

class ExternalPhoto(models.Model):
    filename = models.ImageField(upload_to='external_photos/')
    house = models.ForeignKey(House, related_name='external_photos', on_delete=models.CASCADE)

class Room(models.Model):
    name = models.CharField(max_length=255)
    total_area = models.IntegerField()
    house = models.ForeignKey(House, related_name='rooms', on_delete=models.CASCADE)