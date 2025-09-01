from django.db import models

# Create your models here.
class Resources(models.Model):
    name=models.CharField(max_length=100)
    des=models.CharField()
    img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name