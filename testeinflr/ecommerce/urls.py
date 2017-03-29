from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.products_view),
    url(r'user', views.users_view)

]