from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('tables/', include('tables.urls')),
    path('reservations/', include('reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Встроенные маршруты Django
    path('', lambda request: redirect('/accounts/login/')),  # Перенаправление на страницу логина
]
