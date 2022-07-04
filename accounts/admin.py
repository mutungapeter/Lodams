from django.contrib import admin
from .models import*
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_admin", "is_active", "date_joined")
    search_fields = ("is_admin", "is_active")
