from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('catalog.Book', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return self.product


