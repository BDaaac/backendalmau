from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('customer__name', 'table__number', 'date')

    def save_model(self, request, obj, form, change):
        """Вызываем валидацию перед сохранением в админке"""
        obj.clean()
        super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)
