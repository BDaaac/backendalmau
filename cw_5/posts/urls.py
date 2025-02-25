from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("posts/", views.post_list, name="list"),
    path("posts/my/", views.my_posts, name="my_posts"),
    path("posts/<int:id>/", views.post_detail, name="detail"),
    path("posts/create/", views.post_create, name="create"),
    path("posts/<int:id>/delete/", views.post_delete, name="delete"),
]
