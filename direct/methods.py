from blog.methods import sort_follow_dict
from pairing import pair


def chat_id_creator(request, pk):
    '''
    It will user pairing function where the first number is the lowest pk
    '''
    pk_request = request.user.pk
    pk_reciever = pk
    if pk_request > pk_reciever:
        id = pair(pk_reciever, pk_request)
    else: 
        id = pair(pk_request, pk_reciever)
    return id


def mutuals(request):
    '''
    Just sort the profiles that you follow and they follow you back
    '''
    followers = sort_follow_dict(request)['followers']
    followeds = sort_follow_dict(request)['followeds']
    mutuals = []
    for profile in followeds:
        if profile in followers:
            mutuals.append({
                'profile': profile,
                'id': chat_id_creator(request=request, pk=profile.user.pk)
            })
    return mutuals


