from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'user', views.list_users_view)

]