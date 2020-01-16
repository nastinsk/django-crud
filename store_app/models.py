from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    def __str__(self):
        return self.title
