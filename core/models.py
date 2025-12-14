from django.db import models
from .auth_models import User
import pytz
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=18)

    def __str__(self):
        return self.name


from django.utils import timezone


class Blog(models.Model):
    image = models.FileField(upload_to='blog/', blank=True, null=True)  # mp4 или фото
    title = models.CharField(max_length=56)
    desc = models.CharField(max_length=128)
    create = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title

    @property
    def get_date(self):
        now = timezone.now()
        posted = self.create  # уже aware
        calc = int((now - posted).total_seconds() // 60)

        if calc == 0:
            return "hozirgina"
        if calc < 60:
            return f"{calc} minut oldin"
        if calc < 60 * 24:
            return f"{calc // 60} soat oldin"
        return posted.strftime("%H:%M / %d-%b-%y")
    @property
    def top_comments(self):
        return self.comments.filter(parent__isnull=True)


class Comment(models.Model):
    new = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=32)
    message = models.TextField()
    post = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.message[:20]

    def get_date(self):
        now = timezone.now()
        posted = self.post  # уже aware
        calc = int((now - posted).total_seconds() // 60)

        if calc == 0:
            return "hozirgina"
        if calc < 60:
            return f"{calc} minut oldin"
        if calc < 60 * 24:
            return f"{calc // 60} soat oldin"
        return posted.strftime("%H:%M / %d-%b-%y")