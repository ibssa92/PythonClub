from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getEvents/', views.getEvents, name='events'),
    path('meetingDetail/<int:id>',views.meetingDetail, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginMessage/', views.loginMessage, name='loginmessage'),
    path('logoutMessage/', views.logoutMessage, name='logoutmessage'),
]