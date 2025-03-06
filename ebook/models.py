from django.db import models
from base.models import Base

class Ebook(Base):
    image = models.ImageField(upload_to="ebook/images")
    ebook_file = models.FileField(upload_to="ebook/files")

    def __str__(self):
        return self.title