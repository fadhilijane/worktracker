from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
        user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
                related_name='employee_profile'
                )
        role = models.CharField(max_length=100)
        is_active = models.BooleanField(default=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.user.get_username()
