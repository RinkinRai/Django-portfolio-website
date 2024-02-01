from django.contrib import admin
from django.urls import path,include
from home import views


# Django admin header customization

admin.site.site_header = "Login to Developer Rinki "
admin.site.site_title = "Welcome to Rinki's Dashboard"
admin.site.index_tittle = "Welcome to this Portal" 
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects', views.projects, name='projects'),
    path('contact',views.contact,name='contact')

]   