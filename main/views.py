from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Course, Intake, Subject, Student, Result, Staff
from django.views.generic import ListView, CreateView, DetailView, View, TemplateView, UpdateView
from django.urls import reverse_lazy
from .forms import StudentForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def staff_index(request):
    context = {
        "staff_index": staff_index,
    }
    return render(request, 'staff/staff_base.html', context)

def results_index(request):
    context = {
        "results_index": results_index,
    }
    return render(request, 'base7.html', context)

def courses_index(request):
    context = {
        "courses_index": courses_index,
    }
    return render(request, 'courses/courses-base.html', context)



def intakes_index(request):
    context = {
        "intakes_index": intakes_index,
    }
    return render(request, 'base6.html', context)

def students_index(request):
    context = {
        "students_index": students_index,
    }
    return render(request, 'students/students-base.html', context)

def subjects_index(request):
    context = {
        "subjects_index": subjects_index,
    }
    return render(request, 'base5.html', context)

def mycourses_index(request):
    context = {
        "mycourses_index": mycourses_index,
    }
    return render(request, 'mycourses/mycourses_base.html', context)

def mystudents_index(request):
    context = {
        "mystudents_index": mystudents_index,
    }
    return render(request, 'mystudents/my-students-base.html', context)

def myresults_index(request):
    context = {
        "myresults_index": myresults_index,
    }
    return render(request, 'myresults/my-results-base.html', context)








def index(request):
    context = {
        "index":index,
    }
    return render(request, 'index2.html', context)
"""
def intakes(request):
    intakes = Intake.objects.all()
    context = {
        "intakes": intakes,
    } 
    return render(request, "intakes/intakes.html", context)
"""

"""
class NewIntake(CreateView):
    model = Intake
    fields = "__all__"
    template_name = "intakes/new-intake.html"
    success_url = reverse_lazy("intakes")
"""   
    
def results(request):
    results = Result.objects.all()
    context = {
        "results": results,
    }    
    return render(request, "results/results.html", context)

class UpdateResult(UpdateView):
    model = Result
    fields = "__all__"
    template_name = "main/update-result.html"
    success_url = reverse_lazy("results") 



def my_results(request):
    my_results = Result.objects.filter(student=request.user.student.id)
    context = {
        "my_results": my_results,
    }
    return render(request, "main/my-results.html", context)

def my_students(request):
    my_students =  Student.objects.filter(staff=request.user.staff.id)
    context = {
        "my_students": my_students,
    }
    return render(request, "mystudents/my-students.html", context)

def staffs(request):
    staffs = Staff.objects.all()
    context = {
        "staffs": staffs,
    }
    return render(request, "staff/staff-list.html", context)


def students(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, "students/students.html", context)

def my_courses(request):
    my_courses = Course.objects.filter(staff=request.user.staff.id)
    context = {
        "my_courses": my_courses,
    }
    return render(request, "mycourses/my-courses.html", context)
"""
def Courses(request):
    courses = Course.objects.all()
    context = {
        "courses ": courses,
    }
    return render(request, "main/courses.html", context)
"""
class CoursesList(ListView):
    model = Course
    template_name = 'main/courses.html'

class SubjectsList(ListView):
    model = Subject
    template_name = 'main/subjects.html'

class IntakesList(ListView):
    model = Intake
    template_name = 'main/intakes.html'

"""
def subjects(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects,
    }
    return render(request,"subjects/subjects.html", context)
"""



class NewResult(CreateView):
    model = Result
    fields = "__all__"
    template_name = "results/new-result.html"
    success_url = reverse_lazy("results")


class NewCourse(CreateView):
    model = Course
    fields = "__all__"
    template_name = "main/new-course.html"
    success_url = reverse_lazy("courses")


class NewSubject(CreateView):
    model = Subject
    fields = "__all__"
    template_name = "Main/new-subject.html"
    success_url = reverse_lazy("subjects")
    
class NewStaff(CreateView):
    model = Staff
    fields = "__all__"
    template_name = "staff/new-staff.html"
    success_url = reverse_lazy("staffs")
    
class NewStudent(CreateView):
    model = Student
    fields = "__all__"
    template_name = "students/new-student.html"
    success_url = reverse_lazy("students")

def new_student(request):
    form = StudentForm
    context = {
        "form": form,
    }
    if request.method=="POST":
        user = request.user
        name = request.POST.get("name")
        
        email =request.user.email
        adm_number = request.POST.get("adm_number")

        student = Student()
        student.user=user
        student.name=name
        
        student.email = email
        student.adm_number=adm_number
        student.save()
        return redirect("students")
    return render(request, "students/new-student.html", context)    


class NewIntake(CreateView):
    model = Intake 
    fields = "__all__"
    template_name = "main/new-intake.html"
    success_url = reverse_lazy("intakes")  
    
    
              
   

class UpdateStaff(UpdateView):
    model = Staff
    fields = "__all__"
    template_name = "main/update-staff.html"
    success_url = reverse_lazy("staffs")
    
class UpdateStudent(UpdateView):
    model = Student
    fields = "__all__"
    template_name =  "main/update-student.html"
    success_url = ("students")
    
class UpdateSubject(UpdateView):
    model = Subject
    fields = "__all__"
    template_name = "main/update-subject.html"
    success_url = reverse_lazy("subjects")
    
class UpdateIntake(UpdateView):
    model = Intake
    fields = "__all__"
    template_name = "main/update-intake.html"
    success_url = reverse_lazy("intakes")
    
class UpdateCourse(UpdateView):
    model = Course
    fields = "__all__"
    template_name = "main/update-course.html"
    success_url = reverse_lazy("courses")           


def update_course(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    course = get_object_or_404(Course, pk = pk)
 
    # pass the object as instance in form
    form = CourseForm(request.POST or None, instance = course)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("courses")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "main/new-course.html", context)     
