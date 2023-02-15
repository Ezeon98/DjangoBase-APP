from django.db import models
from django.db.models import ProtectedError

class Product(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    volume = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        raise ProtectedError("Cannot delete a product.", self)
