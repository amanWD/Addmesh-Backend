from django.db import models
from django.contrib.auth import get_user_model
from base.models import Base

User = get_user_model()


class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saves")
    item = models.ForeignKey(Base, on_delete=models.CASCADE, related_name="saves")

    def __str__(self):
        return f"{self.user.name} saved {self.item.title}"
