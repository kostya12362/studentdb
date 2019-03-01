"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from students.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # STUDENTS
    url(r'^$', students_list, name = 'students'),
    url(r'^students/add/$', students_add, name = 'students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name = 'students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_delete, name = 'students_delete'),
    #GROUPS
    url(r'^groups/$', groups_list, name = 'groups'),
    url(r'^groups/add$', groups_add, name = 'groups_add'),
    url(r'^groups/(?P<sid>\d+)/edit/$', groups_edit, name = 'groups_edit'),
    url(r'^groups/(?P<sid>\d+)/delete/$', groups_delete, name = 'groups_delete'),
    #JOURNAL
    url(r'^journal/$', journal_list, name = 'journal'),
    # url(r'^journal/add$', groups_add, name = 'journal_add'),
    # url(r'^journal/(?P<sid>\d+)/edit/$', groups_edit, name = 'journal_edit'),
    # url(r'^journal/(?P<sid>\d+)/delete/$', groups_delete, name = 'journal_delete'),
]