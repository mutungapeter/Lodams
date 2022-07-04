from django.urls import path

from . import views
from .views import NewResult, NewCourse, NewIntake,NewStaff, NewStudent, NewSubject, UpdateResult, UpdateStaff, UpdateStudent, UpdateSubject, UpdateIntake, UpdateCourse, CoursesList, SubjectsList, IntakesList
#from .views import update_course, update_user




urlpatterns = [
    path('', views.index, name="index"),
    #path("courses/", views.all_courses, name="courses"),
    #path("intakes/", views.intakes, name="intakes"),
    path("results/", views.results, name="results"),
    path("my-results/", views.my_results, name ="my-results"),
    path("my-students/", views.my_students, name= "my-students"),
    path("my-courses/", views.my_courses, name="my-courses"),
    #path("subjects/", views.subjects, name="subjects"),
    path("staffs/", views.staffs, name="staffs"),
    path("students/", views.students, name="students"),
    #path("courses/", views.courses, name="courses"),
    path('courses/', CoursesList.as_view(), name="courses"),
    path('subjects/', SubjectsList.as_view(), name="subjects"),
    path('intakes/', IntakesList.as_view(), name="intakes"),
    
    
    path("new-subject/", NewSubject.as_view(), name="new-subject"),
    path("new-course/", NewCourse.as_view(), name="new-course"),
    path("new-student/", NewStudent.as_view(), name="new-student"),
    path("new-intake/", NewIntake.as_view(), name="new-intake"),
    path("new-result/", NewResult.as_view(), name="new-result"),
    path("new-staff/", NewStaff.as_view(), name="new-staff"),
    
    path("staff-index/", views.staff_index, name="staff-index"),
    path("students-index/", views.students_index, name="students-index"),
    path("results-index/", views.results_index, name="results-index"),
    path("courses-index/", views.courses_index, name="courses-index"),
    path("intakes-index/", views.intakes_index, name="intakes-index"),
    path("subjects-index/", views.subjects_index, name="subjects-index"),
    path("mycourses-index/", views.mycourses_index, name="mycourses-index"),
    path("mystudents-index/", views.mystudents_index, name="mystudents-index"),
    path("myresults-index/", views.myresults_index, name="myresults-index"),
    
    
    
    
    
    path("update/<str:pk>/", UpdateResult.as_view(), name="update-result"),
    path("update/<str:pk>/", UpdateStaff.as_view(), name="update-staff"),
    path("update/<str:pk>/", UpdateStudent.as_view(), name="update-student"),
    path("update/<str:pk>/", UpdateSubject.as_view(), name="update-subject"),
    path("update/<str:pk>/", UpdateIntake.as_view(), name="update-intake"),
    #path("update/<str:pk>/", UpdateCourse.as_view(), name="update-course"),
    #path('update/<str:id>/', update_user, name="update-user"),
    path('update/<str:pk>/course/',views.update_course, name="update-course" ),
]

