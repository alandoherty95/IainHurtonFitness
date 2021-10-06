from django.urls import path
from . import views


# Blog app URLs
urlpatterns = [
    path('', views.all_blogposts, name='all_blogposts'),
    path('<int:post_id>/', views.blogpost_detail, name='blogpost_detail'),
    path('add/', views.add_blogpost, name='add_blogpost'),
    path('edit/<int:post_id>', views.edit_blogpost, name='edit_blogpost'),
    path('delete/<int:post_id>', views.delete_blogpost,
         name='delete_blogpost'),
]
