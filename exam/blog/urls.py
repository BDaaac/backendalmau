# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import PostViewSet, CommentViewSet

# 1. Базовый роутер для /api/posts/
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# 2. Вложенный роутер для /api/posts/{post_pk}/comments/
posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

# 3. Собираем все URL
urlpatterns = [
    # GET /api/posts/      — список постов
    # POST /api/posts/     — создать пост
    # GET /api/posts/{pk}/ — получить детали поста
    # PUT/PATCH/DELETE     — обновить/частично обновить/удалить пост
    path('', include(router.urls)),

    # GET /api/posts/{post_pk}/comments/      — список комментариев к посту
    # POST /api/posts/{post_pk}/comments/     — добавить комментарий
    # GET /api/posts/{post_pk}/comments/{pk}/ — детали комментария
    # PUT/PATCH/DELETE                       — обновить/частично/удалить комментарий
    path('', include(posts_router.urls)),
]
