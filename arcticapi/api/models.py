from django.db import models
from api.fields import JSONField

# Create your models here.
class Category(models.Model):
    title = models.TextField()
    #description = models.TextField(uff")

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) #1,234,567,890.00

#In models.py, create the Sale model. 
# The fields are name (TextField), address1 (TextField), address2 (TextField), city (TextField)
# , state (TextField), zipcode (TextField), total (DecimalField), items (JSONField), and payment_intent (JSONField). 
# Run makemigrations and migrate.	

class Sale(models.Model):
    name = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    items = JSONField(default=dict)
    payment_intent = JSONField(default=dict)
    