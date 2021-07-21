from django.urls import path
from my_app import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('dynamic/<id>', views.dynamic, name="dynamic"),
    path('todo/', views.todo, name="todo"),
    path('mark_as_complete/<id>', views.mark_as_complete, name="mark_as_complete"),
    path('delete_todo/<id>', views.delete_todo, name="delete_todo"),
]
