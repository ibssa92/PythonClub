from django.test import TestCase
from .models import Event, Meeting, MeetingMinutes, Resource
import datetime
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase) :
    def test_string(self):
        meeting=Meeting(meetingtitle='Potluck')
        self.assertEqual(str(meeting),meeting.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

class EventTest (TestCase):
    def test_string(self) :
        event=Event(eventtitle='Birthday')
        self.assertEqual(str(event),event.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table),'event')

class MeetingMinutesTest (TestCase):
    def test_string(self):
        minutes=MeetingMinutes(meetingID='2')
        self.assertEqual(str(minutes),minutes.meetingID)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table),'meeting')

class MeetingFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create('username=user1', password='P@ssw0rd1')
        self.type=MeetingType.objects.create(meetingtypename='type1')
    
    def test_meetingForm(self):
        data={
            'meetingtitle' : 'meeting1',
            'meetingagenda' : 'agenda1',
            'meetinglocation' : 'location1', 
           

        }
        form = MeetingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_meetingFormInvalid(self):
        data={
            'meetingtitle' : 'meeting1',
            'meetingagenda' : '',
            'meetinglocation' : 'location1', 
           

        }
        form = MeetingForm(data=data)
        self.assertFalse(form.is_valid())
