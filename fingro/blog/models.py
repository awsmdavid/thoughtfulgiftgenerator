from django.db import models
from django.core.urlresolvers import reverse
 
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['created']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

class GifteeDataForm(models.Model):
    # gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    # hobbies = models.TextField()

# class GifteeData(ModelForm):
#     class Meta:
#         gender = models.CharField(max_length=6, choices=gender)
#         age = models.IntegerField()
#         hobbies = models.TextField()
#         # exclude = ('published', 'likes', 'unlikes', 'created', 'slug', 'postId', 'dateSubmitted')

# class GifteeDataForm(forms.Form):
#     enteredData = forms.CharField(max_length=255)