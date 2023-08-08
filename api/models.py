from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    pub = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'name: {self.title}'
