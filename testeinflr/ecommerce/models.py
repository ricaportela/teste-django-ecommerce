from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Produtos"
        verbose_name_plural = "Produtos"

