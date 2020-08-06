from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.memu_view, name="menu"),
    path('index/', views.main_view, name='index'),
    path('create/', views.create_post, name='create'),
    path('create-safe/', views.create_post_safe, name='create_safe'),
    path('post/<int:id>/', views.post, name='post'),
]
