from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255, null=True, blank=True)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta():
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    text=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingID

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    URL=models.URLField()
    dateentered=models.DateField()
    userID=models.IntegerField()

    def __str__(self):
        return self.resourcename

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255, null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'