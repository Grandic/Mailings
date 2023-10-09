from django.core.cache import cache

from config.settings import CACHE_ENABLE
from .models import Blog



def get_posts():
    if CACHE_ENABLE:
        key = f'posts_list'
        posts_list = cache.get(key)
        if posts_list is None:
            posts_list = Blog.objects.all()
            cache.set(posts_list, posts_list)
    else:
        posts_list = Blog.objects.all()

    return posts_list