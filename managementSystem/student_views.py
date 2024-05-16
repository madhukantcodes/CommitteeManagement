from django.shortcuts import render, redirect
from app.models import *


def home(request):
    user = request.user
    student = Student.objects.filter(admin=user)

    context ={
        'student': student
    }
    return render(request, "student/home.html", context)


def view_meetings(request):
    user = request.user
    student = Student.objects.get(admin=user)
    committee = Committee.objects.get(name=student.committee_id.name)
    meeting = newMeeting.objects.filter(
        leader=committee.leader
    )
    context = {
        'meeting': meeting
    }

    return render(request, 'student/view_meetings.html', context)
