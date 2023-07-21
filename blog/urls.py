from django.urls import path
from blog.views import all_blogs, blog_details, category_blog
urlpatterns = [
    path("", all_blogs, name="all_blogs"),
    path("<int:id>/", blog_details, name="blog_details"),
    path("category/<int:cid>/", category_blog, name="blog_category"), 
]