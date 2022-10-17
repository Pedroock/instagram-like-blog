from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import UsersProfile
from .methods import mutuals, chat_id_creator
from django.contrib.auth.models import User
from pairing import depair
# Create your views here.
@login_required
def direct_index(request):
    context = {
        'mutuals': mutuals(request)
    }
    return render(request, 'direct/direct_index.html', context)


@login_required
def direct_chat(request, id):
    '''
    The first number on the depair is the request.user.pk and the other is the reciever pk
    '''
    # sort pks
    for x in depair(id):
        if x == request.user.pk:
            pk_request = x
        else:
            pk_reciever = x
    reciever = UsersProfile.objects.filter(user=User.objects.filter(pk=pk_reciever).first()).first()
    context = {
        'mutuals': mutuals(request),
        'reciever': reciever,
        'room_name': id,
    }
    return render(request, 'direct/direct_chat.html', context)
