from .views import table_list, available_tables
from django.urls import path
from .views import add_table, edit_table, delete_table

urlpatterns = [
    path('', table_list, name='tables_list'),  # ✅ Должно быть name='tables_list'
    path('available/', available_tables, name='tables_available'),
    path('', table_list, name='tables_list'),
    path('add/', add_table, name='add_table'),
    path('edit/<int:id>/', edit_table, name='edit_table'),
    path('delete/<int:id>/', delete_table, name='delete_table'),
]


