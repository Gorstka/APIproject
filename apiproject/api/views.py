from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Comment, Post
from .serializers import (
    CommentSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering = ("-pub_date",)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        comments = Comment.objects.filter(post=post_id)
        return comments
