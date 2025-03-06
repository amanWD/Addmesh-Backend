from django.contrib import admin

from .models import ExplanationAudio, Chapter, AudioFile

admin.site.register(ExplanationAudio)
admin.site.register(Chapter)
admin.site.register(AudioFile)
