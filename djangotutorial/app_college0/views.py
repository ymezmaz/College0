from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    return HttpResponse(render(request, "app_college0/Landing.jsx"))
    
def submit_student_app(request, s_name, s_gpa, desired_major):
    s_app = Student_Apply(name=s_name, gpa=float(s_gpa), prog=desired_major)
    s_app.save()
    y = Student_Apply.objects.get(name=s_name, gpa=float(s_gpa))
    return HttpResponse("Your application id is %s" % y.app_id)
    
def submit_instructor_app(request, i_name):#intend to improve, along with model of instructor app
    i_app = Instructor_Apply(name=i_name)
    i_app.save()
    y = Instructor_Apply.objects.get(name=i_name)
    return HttpResponse("Your application id is %s" % y.app_id)
    
def submit_grad_app(request, student):
    g_app = GradApply(applicant=student)
    g_app.save()
    
def submit_complaint(request, s_id, target_id, msg):
    comp = Complaint(source=s_id, target=target_id, text=msg)
    comp.save()

