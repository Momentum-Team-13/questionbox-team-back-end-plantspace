from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<User username={self.username} pk={self.pk}>'

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=125)
    body = models.TextField(max_length=250)
