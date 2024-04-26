from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ("ნაჭრის მხარჩანთა", "ნაჭრის მხარჩანთა"),
        ('ნაჭრის ზურგჩანთა', "ნაჭრის ზურგჩანთა"),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="no description")
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
        image = models.ImageField(upload_to="product", max_length=100, null=True)
        image = models.URLField()

