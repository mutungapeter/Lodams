from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
#from .views import UpdateUser
from .views import *

urlpatterns = [
    path('index2/', views.index2, name="index2"),
    path('', views.login_views, name="login"),
    path("logout/", views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path("users/", views.users_list, name="users"),
    #path("student-users/", views.student_users, name="student-users"),
    path("update/<str:pk>/", UpdateUser.as_view(), name="update-user"),
    #path("update/<str:pk>/", views.update_user, name="update-user"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name = "reset_passowrd"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name = "password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name = "password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name = "password_reset_complete"),
    #path('update/<str:id>/', update_user, name="update-user"),
]