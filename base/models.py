from django.db import models
import uuid

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    TYPE_CHOICE = (("blog", "BLOG"),("ebook", "EBOOK"), ("audio book", "AUDIO BOOK"),("explanation audio", "EXPLANATION AUDIO"), ("event", "EVENT"))
    type = models.CharField(choices=TYPE_CHOICE)
    description = models.TextField()
    price_in_etb = models.FloatField(default=0.0)
    price_in_usd = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title