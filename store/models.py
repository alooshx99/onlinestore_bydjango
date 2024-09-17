from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    price = models.BigIntegerField()
    

    def __str__(self):
        return self.name


class Transaction(models.Model):
    product_id = models.ForeignKey(Product, related_name="transactions", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.BigIntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product_id.price * self.quantity
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id.name} - {self.quantity} pcs"
