from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])