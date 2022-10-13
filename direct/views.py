from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UsersProfile
from .methods import mutuals
# Create your views here.
@login_required
def direct_index(request):
    context = {
        'mutuals': mutuals(request)
    }
    return render(request, 'direct/direct_index.html', context)


@login_required
def direct_chat(request, pk):
    context = {
        'mutuals': mutuals(request),
        'reciever': UsersProfile.objects.filter(pk=pk).first()
    }
    return render(request, 'direct/direct_chat.html', context)
