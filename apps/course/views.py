from django.shortcuts import render, redirect
from .models import Course 

def index(request):
	context = {
		"courses": Course.objects.all()
	}
	return render(request, "course/index.html", context)

def create(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect('/')

def destroy(request, id):
	course = Course.objects.get(id=id)
	if request.method =='POST':
		course.delete()
		return redirect('/')
	else:
		context = {
			"course": course
		}
		return render(request, "course/delete.html", context)
