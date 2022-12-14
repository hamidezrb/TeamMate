
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("posts", views.posts, name="posts"),
    path("participants/<int:team_id>", views.participants, name="participants"),
    path("following", views.following, name="following"),
    path("following_posts", views.following_posts, name="following_posts"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow_user", views.follow_user, name="follow_user"),
    path("profile_posts/<int:id>", views.profile_posts, name="profile_posts"),
    path("team_request/<int:team_id>", views.team_request, name="team_request"),
    path("Accept/<int:request_id>", views.Accept, name="Accept"),
    path("new_Team", views.new_Team, name="new_Team"),
    path("edit_profile", views.edit_profile, name="edit_profile")
    
]
