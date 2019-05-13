from django.shortcuts import render, get_object_or_404
from .models import Event, Meeting, MeetingMinutes, Resource

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getMeetings(request):
    meetings_list=Meeting.objects.all()
    context={'meetings_list' : meetings_list}
    return render(request, 'Club/meetings.html', context=context)

def getEvents(request) :
    events_list=Event.objects.all()
    return render(request, 'Club/events.html', {'events_list' : events_list})

def meetingDetail (request, id): 
    meet=get_object_or_404(Meeting, pk=id)
    minutescount=MeetingMinutes.objects.filter(meetingID=id).count()
    minutes=MeetingMinutes.objects.filter(meetingID=id)
    context={
        'meet' : meet, 
        'minutescount' : minutescount,
        'minutes' : minutes,

    }

    return render (request, 'Club/meetingdetail.html', context=context)
