from django.test import TestCase
from .models import Event, Meeting, MeetingMinutes, Resource

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

