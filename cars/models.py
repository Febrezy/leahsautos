from django.db import models


class Cars(models.Model):
    title = models.CharField(max_length=20)
    miles = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='cars/images/')
    url = models.URLField(blank=True)
