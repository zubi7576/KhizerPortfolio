from django.urls import path
from LandingPage import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('projects/',views.projects,name="projects"),
    path('services/',views.services,name="services"),
    path('process/',views.process,name="process"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]
