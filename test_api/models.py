from django.db import models

class Article(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.FloatField(default=0.0)
    customer=models.CharField(max_length=50)