from django.db import models
from config import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='products',blank=True,null=True)
    metal = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    @property
    def avg_rate(self):
        rates = [i.rate for i in self.comments.all() if i.rate > 0]

        if rates:
            return round(sum(rates) / len(rates), 1)
        return 0


class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_comments')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    text=models.TextField()
    rate=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image_comment=models.ImageField(upload_to='comment/',blank=True,null=True)

    def __str__(self):
        return self.text