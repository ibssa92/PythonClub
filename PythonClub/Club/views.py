from django.shortcuts import render
from .models import Event, Meeting, MeetingMinutes, Resource

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getMeetings(request):
    meetings_list=Event.objects.all()
    context={'meetings_list' : meetings_list}
    return render(request, 'Club/meetings.html', context=context)
