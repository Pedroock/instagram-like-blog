from blog.methods import sort_follow_dict


def mutuals(request):
    '''
    Just sort the profiles that you follow and they follow you back
    '''
    followers = sort_follow_dict(request)['followers']
    followeds = sort_follow_dict(request)['followeds']
    mutuals = []
    for profile in followeds:
        if profile in followers:
            mutuals.append(profile)
    return mutuals