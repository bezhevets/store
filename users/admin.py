from django.contrib import admin

from products.admin import BasketAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["last_name"]
    inlines = [BasketAdmin]
