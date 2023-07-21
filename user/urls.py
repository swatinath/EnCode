from django.urls import path
from user import views
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("profile/", views.profile, name="profile"),
    path("add_blog/", views.add_blog, name="add_blog"),
    path("signout/", views.signout, name="signout"),
]
