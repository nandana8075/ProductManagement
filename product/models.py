from django.db import models

class ProductDb(models.Model):
    product_name=models.CharField(max_length=100)
    product_code=models.IntegerField()
    category=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    stock_quantity=models.IntegerField()

    def __str__(self):
        return self.product_name

