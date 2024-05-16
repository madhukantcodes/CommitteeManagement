from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    leader_count = Leader.objects.all().count()
    committee_count = Committee.objects.all().count()
    committees = Committee.objects.all()
    context = {
        'student_count': student_count,
        'leader_count': leader_count,
        'committee_count': committee_count,
        'committees': committees,
    }

    return render(request, 'hod/home.html', context)


@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    committee = Committee.objects.all()

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
        committee_id = request.POST.get('committee_id')

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
            return redirect('add_student')

    context = {
        'courses': course,
        'committees': committee,
    }

    return render(request, 'hod/add_student.html', context)


@login_required(login_url='/')
def view_student(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, "hod/view_student.html", context)


@login_required(login_url='/')
def edit_student(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'courses': course,
    }
    return render(request, 'hod/edit_student.html', context)


@login_required(login_url='/')
def delete_student(request, admin):
    student = CustomUser.objects.filter(id=admin)
    student.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('view_student')


@login_required(login_url='/')
def add_leader(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

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
                user_type=2
            )
            user.set_password(password)
            user.save()
            leader = Leader(
                admin=user,
                address=address,
                gender=gender
            )
            leader.save()
            messages.success(request, "Leader Successfully Added")
            return redirect('add_leader')

    return render(request, "hod/add_leader.html")


@login_required(login_url='/')
def view_leader(request):
    leader = Leader.objects.all()
    context = {
        'leader': leader
    }
    return render(request, 'hod/view_leader.html', context)


@login_required(login_url='/')
def delete_leader(request, admin):
    leader = CustomUser.objects.filter(admin=admin)
    leader.delete()
    messages.success(request, "Leader deleted successfully")
    return redirect('view_leader')


def add_committee(request):
    leaders = Leader.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        leader_id = request.POST.get('leader_id')

        leader = Leader.objects.get(id=leader_id)

        committee = Committee(
            name=name,
            description=description,
            leader=leader
        )
        committee.save()
        messages.success(request, "Committee Successfully Added")

    context = {
        'leader': leaders
    }
    return render(request, "hod/add_committee.html", context)


def view_committee(request):
    committees = Committee.objects.all()

    context = {
        'committees': committees
    }
    return render(request, "hod/view_committee.html", context)


def delete_committee(request, id):
    committee = Committee.objects.filter(id=id)
    committee.delete()
    messages.success(request, "Committee successfully Deleted")
    return redirect("view_committee")


def send_leader_notification(request):

    return render(request, "hod/leader_notification.html")
