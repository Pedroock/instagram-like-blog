from django.shortcuts import render
from users.forms import UsersFollowersForm
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from users.models import UsersFollowers
# Create your views here.
@csrf_exempt
def AjaxProfileFollow(request):
    if request.method == 'POST':
        form = UsersFollowersForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # serializar é transforma info pra o ajax joga pro outro lado
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    else:
        return JsonResponse({"error": form.erros}, status=400)
        # 200 deu certo, 400 deu nn


@csrf_exempt
def AjaxProfileUnfollow(request):
    if request.method == 'POST':
        form = UsersFollowersForm(request.POST)
        if form.is_valid():
            print('form is valid')
            follower = form.cleaned_data['follower']
            followed = form.cleaned_data['followed']
            instance = UsersFollowers.objects.filter(follower=follower, followed=followed).first()
            instance.delete()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error'}, status=400)
    else:
        return JsonResponse({'status': 'error'}, status=400)
        # 200 deu certo, 400 deu nn