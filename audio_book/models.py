from django.db import models
from base.models import Base


class AudioBook(Base):
    image = models.ImageField(upload_to="audio_book/images")

    def __str__(self):
        return self.title
    

class AudioFile(models.Model):
    audio_file = models.FileField(upload_to="audio_book/files")
    audio_book = models.ForeignKey(AudioBook, related_name="playlist", on_delete=models.CASCADE)

