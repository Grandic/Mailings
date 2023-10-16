from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, index

app_name = BlogConfig.name

urlpatterns = [
    path('list_posts', PostListView.as_view(), name='list_posts'),
    path('', index, name='index'),
    path('detail_post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
]
