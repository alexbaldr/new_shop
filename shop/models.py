from django.db import models
from authentication.models import User
from main.models import Book

class Basket(models.Model):
    user = models.ForeignKey (User, related_name='basket', on_delete=models.CASCADE)
    book = models.ForeignKey (Book, on_delete=models.CASCADE)
    total = models.DecimalField(default=0)