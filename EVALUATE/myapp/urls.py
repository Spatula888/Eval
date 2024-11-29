from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="index"),  # Ensure you have a proper name for the home route
    path('login/', views.student_login, name="student_login"),  # Add the login route
    
    path('management-dashboard/', views.management_dashboard, name="management_dashboard"),
    path('', views.home, name="index"),

    path('management-login/', views.management_login, name="management_login"),
    

]
