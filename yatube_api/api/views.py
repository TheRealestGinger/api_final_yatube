from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Post, Follow
from .permissions import OwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Добавляет автора к посту."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        return self.get_post(self.kwargs['post_id']).comments.all()

    def perform_create(self, serializer):
        """Добавляет автора к комментарию."""
        serializer.save(
            author=self.request.user,
            post=self.get_post(self.kwargs['post_id'])
        )

    def get_post(self, id):
        return get_object_or_404(Post, id=id)


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для подписок."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        if self.request.user == serializer.validated_data['following']:
            raise serializers.ValidationError(
                "Вы не можете подписаться на себя."
            )
        if Follow.objects.filter(
            user=self.request.user,
            following=serializer.validated_data['following']
        ).exists():
            raise serializers.ValidationError("Вы уже подписаны.")
        serializer.save(user=self.request.user)
