from django.db import models

# Create your models here.

class House(models.Model):

    """model definition for houses"""

    name=models.CharField(max_length=140)
    price=models.PositiveBigIntegerField()
    description=models.TextField()
    address=models.CharField(max_length=140)

