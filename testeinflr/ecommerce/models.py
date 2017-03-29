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

class User(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class Meta():
        verbose_name = "Usuarios"
        verbose_name_plural = "Usuarios"

