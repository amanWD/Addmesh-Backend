from django.db import models
from django.contrib.auth import get_user_model
from base.models import Base

User = get_user_model()


class MyShelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    item = models.ForeignKey(Base, on_delete=models.CASCADE, related_name="purchasers")
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} purchased {self.item.title}"
