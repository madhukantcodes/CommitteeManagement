from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages


def home(request):
    user = request.user
    leader = Leader.objects.get(admin=user)
    committee = Committee.objects.filter(leader=leader)
    comm = Committee.objects.get(leader=leader)
    student_count = Student.objects.filter(committee_id=comm).count()

    context = {
        'committee': committee,
        'student_count': student_count,
    }
    return render(request, 'leader/home.html', context)


def view_student(request):
    user = request.user
    leader = Leader.objects.get(admin=user)
    committee = Committee.objects.get(leader=leader)
    student = Student.objects.filter(committee_id=committee)
    context = {
        'student': student,
        'committee': committee,
    }

    return render(request, "leader/view_student.html", context)


def add_student(request):
    course_ = Course.objects.all()
    committee_ = Committee.objects.all()
    context = {
        'course': course_,
        'committees': committee_,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        committee_id = request.POST.get('committee')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "email already exist")
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "username already exist")
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            committee = Committee.objects.get(id=committee_id)

            student = Student(
                admin=user,
                address=address,
                gender=gender,
                date_of_birth=dob,
                course_id=course,
                committee_id=committee,
            )
            student.save()
            messages.success(request, "Student added successfully")
            return redirect('leader_add_student')

    return render(request, 'leader/add_student.html', context)


def add_meeting(request):
    user = request.user
    leader = Leader.objects.get(admin=user)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        venue = request.POST.get('venue')

        meeting = newMeeting(
            leader=leader,
            meeting_date=date,
            meeting_time=time,
            venue=venue,
            meeting_description=description
        )
        meeting.save()
        messages.success(request, "successfully scheduled a meeting!!")

    return render(request, 'leader/add_meeting.html')


def view_meeting(request):
    user = request.user
    leader = Leader.objects.get(admin=user)
    meetings = newMeeting.objects.filter(leader=leader)
    context = {
        'meetings': meetings,
    }
    return render(request, 'leader/view_meeting.html', context)


def delete_meeting(request, id):
    meeting = newMeeting.objects.filter(id=id)
    meeting.delete()
    messages.success(request, "Meeting deleted!")
    return redirect('view_meeting')
