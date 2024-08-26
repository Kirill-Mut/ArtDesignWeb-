from django.db import models





class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
