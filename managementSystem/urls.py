"""
URL configuration for Committee Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views, hod_views, leader_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),

    # login paths
    path('', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout/', views.doLogout, name='logout'),

    # profile update
    path('profile/', views.profile, name='profile'),
    path('Profile/update/', views.profile_update, name='profile_update'),

    # hod panel
    path('Hod/Home', hod_views.HOME, name='hod_home'),
    path('Hod/Student/Add', hod_views.add_student, name='add_student'),
    path('Hod/Student/View', hod_views.view_student, name='view_student'),
    path('Hod/Student/Edit/<str:id>', hod_views.edit_student, name='edit_student'),
    path('Hod/Student/Delete/<str:admin>', hod_views.delete_student, name='delete_student'),


    path('Hod/Leader/Add', hod_views.add_leader, name='add_leader'),
    path('Hod/Leader/View', hod_views.view_leader, name='view_leader'),
    path('Hod/Leader/Delete/<str:admin>', hod_views.delete_leader, name='delete_leader'),
    path('Hod/Leader/SendNotification', hod_views.send_leader_notification, name='send_leader_notification'),

    path('Hod/Committee/Add', hod_views.add_committee, name='add_committee'),
    path('Hod/Committee/View', hod_views.view_committee, name='view_committee'),
    path('Hod/Committee/Delete/<str:id>', hod_views.delete_committee, name='delete_committee'),

    #Leader panel

    path('Leader/Home', leader_views.home, name='leader_home'),
    path('Leader/Student/View', leader_views.view_student, name='leader_view_student'),
    path('Leader/Add/Student', leader_views.add_student, name='leader_add_student'),

    path('Leader/Leader/Add/NewMeeting', leader_views.add_meeting, name='add_meeting'),
    path('Leader/View/Meetings', leader_views.view_meeting, name='view_meeting'),
    path('Leader/Meeting/Delete/<str:id>', leader_views.delete_meeting, name='delete_meeting'),

    #student
    path('Student/Home', student_views.home, name='student_home'),
    path('Student/View/Meetings', student_views.view_meetings, name='student_view_meetings')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
