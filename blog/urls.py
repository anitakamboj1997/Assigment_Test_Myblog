from django.urls import path
from blog.views import BlogPageView, create_post
urlpatterns = [
    path('', BlogPageView.as_view(), name='home'),
    path('add_post/', create_post, name='add_post'),

]
