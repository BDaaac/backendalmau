# myblog/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet
from rest_framework_nested import routers

# --- базовый роутер ---
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# --- вложенный роутер для комментариев ---
posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    # вместо 'api/' просто в корень
    path('', include(router.urls)),
    path('', include(posts_router.urls)),

    path('api-auth/', include('rest_framework.urls')),

    path('api/', include('blog.urls')),

]
