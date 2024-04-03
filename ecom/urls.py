from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("department",views.department_view,name='department'),
    path("register",views.register_view,name='register'),
    path("contact",views.contact,name='contact'),
    path("login",views.login_view,name='login'),
    path("dashboard",views.dashboard_view,name="dashboard"),
    path("booking",views.booking,name="booking"),
    path("student",views.student,name="student"),
    path("add-student/",views.add_student,name="add-student")
]
