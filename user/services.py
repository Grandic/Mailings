from django.core.cache import cache

from config.settings import CACHE_ENABLE
from .models import User


def get_users():
    if CACHE_ENABLE:
        key = f'users_list'
        users_list = cache.get(key)
        if users_list is None:
            users_list = User.objects.all()
            cache.set(users_list, users_list)
    else:
        users_list = User.objects.all()

    return users_list