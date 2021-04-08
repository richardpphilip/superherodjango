from django.urls import path
from . import views


app_name = 'superhero_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('delete/<int:superhero_id>/', views.delete, name='delete'),
    path('update/<int:superhero_id>/', views.update, name='update')
]
