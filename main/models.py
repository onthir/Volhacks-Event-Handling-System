from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, related_name="created_by",on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add= True)
    volunteers = models.ManyToManyField(User, related_name="volunteers")
    closed     = models.BooleanField(default=False)
    hits       = models.IntegerField(default=0, blank=True, null=True)
    image      = models.ImageField(default=None, blank=True, null=True)
    slug       = models.SlugField(unique=True, max_length=1000)
    
    def __str__(self):
        return self.event_name

    # get unique sluf for each event
    def _get_unique_slug(self):
        slug = slugify(self.event_name)
        unique_slug = slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    # for sitemaps
    def get_absolute_url(self):
        return '/details/%s' %self.slug

# table for all the tasks under an event
class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, related_name="created_by_user",on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# comments for each tasks
class TaskComment(models.Model):
    task = models.ForeignKey(Task, related_name="task",on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, related_name="posted_by",on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.posted_by.username
        
