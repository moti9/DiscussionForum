from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from requests import request
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(default=None)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default=None)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.author.username}-{self.title[:25]}"

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username}-{self.subject[:25]}"


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    # upvote=models.BooleanField()

    def __str__(self):
        return f"{self.post.title[:25]}-{self.voter.username}"
