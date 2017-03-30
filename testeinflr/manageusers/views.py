from django.shortcuts import render
from manageusers.models import User


# Create your views here.
def list_users_view(request):
    queryusers = User.objects.all()
    context = {
        "object_list": queryusers
    }
    return render(request, 'list_users.html', context)

