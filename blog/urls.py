from django.urls import path
from blog.views import all_blogs, blog_details, category_blog, add_blogs, add_feedback
urlpatterns = [
    path("", all_blogs, name="all_blogs"),
    path("<int:id>/", blog_details, name="blog_details"),
    path("category/<int:cid>/", category_blog, name="blog_category"),
    path("add_blogs/", add_blogs, name="add_blogs"),
    path("add_feedback/", add_feedback, name="add_feedback"), 
]