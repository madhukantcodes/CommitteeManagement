from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER = [
        (1, 'HOD'),
        (2, 'Leader'),
        (3, 'Student'),
    ]

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pics')


class Leader(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Course description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Committee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    committee_id = models.ForeignKey(Committee, on_delete=models.CASCADE, default=1)

    date_of_birth = models.DateField()

    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class LeaderNotification(models.Model):
    leader_id = models.ForeignKey(Leader, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.leader_id.admin.first_name


class newMeeting(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    venue = models.CharField(max_length=100, default="DG Room")

    def __str__(self):
        return f"Meeting on {self.meeting_date} led by {self.leader.admin.first_name}"
