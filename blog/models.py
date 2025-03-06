from django.db import models
from base.models import Base

class Blog(Base):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Attachments(models.Model):
    reference_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="blog/images", blank=True, null=True)
    blog = models.ForeignKey(Blog, related_name="attachments", on_delete=models.CASCADE)

    def __str__(self):
        return self.reference_name