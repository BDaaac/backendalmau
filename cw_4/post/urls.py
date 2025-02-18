from django.urls import path
from . import views

urlpatterns = [
    path('',views.thread_list,name='thread_list'),
    path('<int:id>/',views.post_to_thread,name='post_to_thread'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('<int:id>/delete/',views.thread_delete,name='thread_delete'),
    path('threads/<int:id>/edit/', views.thread_edit, name='thread_edit'),
]