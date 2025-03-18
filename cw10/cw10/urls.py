from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),  # Теперь API доступен прямо по "/"
    path('admin/', admin.site.urls),
]
