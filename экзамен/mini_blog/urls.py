from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet
from blog import views
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # вложенные комментарии
    path('api/posts/<int:post_pk>/comments/', CommentViewSet.as_view({
        'get':'list','post':'create'
    }), name='comment-list'),
    path('', views.post_list, name='post-list'),
    path('', views.post_list, name='post-list'),

    # Создание нового поста
    path('posts/create/', views.post_create, name='post-create'),

    # Просмотр детали поста и добавление комментариев
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),

    # Редактирование поста
    path('posts/<int:pk>/edit/', views.post_update, name='post-update'),

    # Удаление поста
    path('posts/<int:pk>/delete/', views.post_delete, name='post-delete'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # обновить access
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/register/', views.register, name='register'),

    path('accounts/login/',  auth_views.LoginView.as_view(template_name='blog/login.html'),  name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='post-list'),          name='logout'),



]

