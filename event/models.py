from django.db import models
from base.models import Base


class Event(Base):
    EVENT_TYPE_CHOICE = (("face to face", "FACE TO FACE"), ("online", "Online"))
    event_type = models.CharField(choices=EVENT_TYPE_CHOICE)
    link = models.CharField()
    starting_day = models.DateTimeField()
    ending_day = models.DateTimeField()
    number_of_sites = models.IntegerField(blank=True, null=True)
    round = models.IntegerField()

    def __str__(self):
        return self.title