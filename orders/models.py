from django.db import models
from django.contrib.auth import get_user_model
from base.models import Base
import uuid

User = get_user_model()


class Order(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Base, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id} - Status: {'paid' if self.paid else 'not paid'}"
