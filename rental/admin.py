from django.contrib import admin
from .models import Equipment, Request

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    list_filter = ("price",)
    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "price", "image", "description")
        }),
        ("Характеристики", {
            "fields": ("max_load", "boom_length", "max_height", "axles", "wheel_formula", "dimensions", "extra_specs")
        }),
    )

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone", "email")
    list_filter = ("created_at",)
