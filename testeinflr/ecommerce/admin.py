from django.contrib import admin
from .models import Product

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "url", "description"]
    list_display_links = ["url"]
    search_fields = ["name"]
    class Meta:
        model = Product



admin.site.register(Product, ProductModelAdmin)


