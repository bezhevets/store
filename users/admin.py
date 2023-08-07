from django.contrib import admin

from users.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["last_name"]
