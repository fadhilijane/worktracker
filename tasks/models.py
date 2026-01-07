from django.db import models
from django.contrib.auth.models import User
from employees.models import Employee

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Assigned to: {self.assigned_to})"


class WorkLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='work_logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='work_logs')
    work_date = models.DateField()
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 3.5 hours
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WorkLog for {self.task.title} by {self.employee.user.username} on {self.work_date}"

