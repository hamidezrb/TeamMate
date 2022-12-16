
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("teams", views.teams, name="teams"),
    path("participants/<int:team_id>", views.participants, name="participants"),
    path("following", views.following, name="following"),
    path("following_teams", views.following_teams, name="following_teams"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow_user", views.follow_user, name="follow_user"),
    path("profile_teams/<int:id>/<int:type>", views.profile_teams, name="profile_teams"),
    path("team_request/<int:team_id>", views.team_request, name="team_request"),
    path("accept_member", views.accept_member, name="accept_member"),
    path("new_Team", views.new_Team, name="new_Team"),
    path("edit_profile", views.edit_profile, name="edit_profile")
    
]
