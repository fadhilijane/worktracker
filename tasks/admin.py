from django.contrib import admin
from .models import Task, WorkLog

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'due_date', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title', 'assigned_to__user__username')

@admin.register(WorkLog)
class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'employee', 'work_date', 'hours_spent')
    search_fields = ('task__title', 'employee__user__username')
    list_filter = ('work_date',)

