
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rooms.html', views.rooms, name="rooms"),
    path('contact.html', views.contact, name="contact"),
    path('blog.html', views.blog, name="blog"),
    path('services.html', views.services, name="services"),
    path('about-us.html', views.aboutus, name="aboutus"),
]