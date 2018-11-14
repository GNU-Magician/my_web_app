from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200, help_text='Type the name of the field.')
    pub_date = timezone.now()
    post_content = models.TextField(help_text='Type in the blog post.')

    def __str__(self):
        return self.post_title