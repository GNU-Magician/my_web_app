from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200, help_text='Type the name of the field.')
    pub_date = models.DateTimeField(default=timezone.now)
    post_content = models.TextField(help_text='Type in the blog post.')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def current_time(self):
        return timezone.now()

    def __str__(self):
        return self.post_title
    class Meta:
        permissions = (("can_delete_posts", "Manage posts as needed"),)