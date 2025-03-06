from django.db import models
from base.models import Base

class ExplanationAudio(Base):
    image = models.ImageField(upload_to="explanation_audio/images")
    # event = models.ForeignKey(Event, related_name="event", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    explanation_audio = models.ForeignKey(ExplanationAudio, related_name="chapters", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.explanation_audio.title}"


class AudioFile(models.Model):
    audio_file = models.FileField(upload_to="explanation_auido/files")
    playlist = models.ForeignKey(Chapter, related_name="playlist", on_delete=models.CASCADE) 