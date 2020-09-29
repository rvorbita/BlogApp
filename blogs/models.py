from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """create a blogpost model"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """string representation of the blogpost"""
        return f"{self.title}"

    
    