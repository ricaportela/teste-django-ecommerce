from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^produtos$', views.products_view)
]