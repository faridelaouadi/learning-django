from django.db import models

# Create your models here.
# This is where we create our database


class Tutorials(models.Model):
    tutorial_title = models.CharField(max_length= 200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Title : {self.tutorial_title}"
