from django.urls import path
from .views import reservation_list, add_reservation, edit_reservation, delete_reservation

urlpatterns = [
    path('', reservation_list, name='reservations_list'),
    path('add/', add_reservation, name='add_reservation'),
    path('edit/<int:id>/', edit_reservation, name='edit_reservation'),
    path('delete/<int:id>/', delete_reservation, name='delete_reservation'),  # ✅ Убедись, что здесь <int:id>
]
