from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<User username={self.username} pk={self.pk}>'

class BaseModel(models.Model):
    # Both attributes need options
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()