from django.urls import path
from .import views
app_name = "discussion"

urlpatterns = [
    path('create/', views.create_post, name="createpost"),
    path('', views.home, name="home"),
    path('userposts/<int:pk>', views.userposts, name="userposts"),
    path('post/<int:pk>', views.post, name="post"),
    path('<int:pk>/upvote', views.upvote, name='upvote'),
    path('<int:pk>/downvote', views.downvote, name='downvote'),
]
