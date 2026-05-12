from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_student_app/<str:s_name>/<str:s_gpa>/<str:desired_major>", views.submit_student_app, name="submit_student_app"),
    path("submit_instructor_app/<str:i_name>", views.submit_instructor_app, name="submit_instructor_app"),
    path("submit_grad_app/<int:student>", views.submit_grad_app, name="submit_grad_app"),
    path("submit_complaint/<int:s_id>/<int:target_id>/<str:msg>", views.submit_complaint, name="submit_complaint"),
]

