from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
# blog/views.py

from django.contrib.auth.models import User
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Post, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    RegisterSerializer
)
from .permissions import IsOwnerOrReadOnly


class RegisterView(generics.CreateAPIView):
    """
    Регистрация нового пользователя на /api/register/
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD для постов
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD для комментариев к конкретному посту
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post__pk=post_id).order_by('created_at')

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)

class PostViewSet(viewsets.ModelViewSet):
    queryset         = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends  = [filters.SearchFilter]
    search_fields    = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class   = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # если URL /posts/{post_pk}/comments/
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post__pk=post_id).order_by('created_at')

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)
from rest_framework import generics, permissions
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
