from django.db import models





class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    


class House(models.Model):
    title = models.CharField(max_length=200)
    model_3d = models.FileField(upload_to='3d_models/')
    description = models.TextField()
    total_area = models.FloatField()
    effective_area = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.TextField()  
    blueprint = models.FileField(upload_to='blueprints/')
    exterior_photos = models.ImageField(upload_to='exterior_photos/', blank=True)
    interior_photos = models.ImageField(upload_to='interior_photos/', blank=True)

    def __str__(self):
        return self.title
