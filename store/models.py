from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = (("seller", "Seller"), ("customer", "Customer"), ("viewer", "Viewer"))

    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="store_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="store_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    price = models.BigIntegerField()
    seller = models.ForeignKey(
        User,
        related_name="products",
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "seller"},
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    product_id = models.ForeignKey(
        Product, related_name="transactions", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    total_price = models.BigIntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        User,
        related_name="transactions",
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "customer"},
    )

    def save(self, *args, **kwargs):
        self.total_price = self.product_id.price * self.quantity
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.id} - {self.product.name} by {self.customer.username}"
