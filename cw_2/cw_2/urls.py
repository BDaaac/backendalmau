from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('post.urls')),
    path('', lambda request: redirect('post_list', permanent=True)),  # Редирект на список постов
]
