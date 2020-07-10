from django.conf.urls import url, include, re_path
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.urls import path

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                              template_name="blog/blog.html")),
    re_path(r'(?P<pk>\d+)', DetailView.as_view(model=Post,
                                               template_name="blog/post.html"))
]
