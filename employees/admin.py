from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'is_active', 'created_at')
    list_filter = ('is_active', 'role')
    search_fields = ('user__username', 'user__email')
