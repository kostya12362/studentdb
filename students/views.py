# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Віталій',
		 'last_name': u'Подоба',
		 'ticket': 235,
		 'image': 'img/123.jpg'},
		 {'id': 2,
		 'first_name': u'Костя',
		 'last_name ': u'Остапенко',
		 'ticket': 2123,
		 'image': 'img/234.jpg'},
		 {'id': 3,
		  'first_name': u'Павло',
		  'last_name': u'Лисенко',
		  'ticket': 123,
		  'image': 'img/456.jpeg'}
		)
		
		
		
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1> Students Add Form </h1>')

def students_edit(request, sid):
	return HttpResponse('<h1> Edit Students %s </h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1> Delete Students %s </h1>' %sid)

# Views for Groups

def groups_list(request):
	groups = (
		{'id': 1,
		 'first_name': u'Віталій',
		 'last_name': u'Подоба',
		 'num': 'МтМ-1',
		 },
		 )
	return render(request, 'students/grups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>GroupAdd Form </h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1> Edit Group %s</h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' %gid)

def journal_list(request):
	return render(request, 'students/journal_list.html', )