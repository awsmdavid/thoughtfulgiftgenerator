from django.db import models
from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm
 
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

AGE_CHOICES = (
    ('age_1', '0-5'),
    ('age_2', '6-13'),
    ('age_3', '14-20'),
    ('age_4', '21-34'),
    ('age_5', '35-59'),
    ('age_6', '60+'),
)

PRICE_CHOICES = (
    ('price_1', '$0-20'),
    ('price_2', '$20-50'),
    ('price_3', '$50-100'),
    ('price_4', '$100+'),    
)

class GiftIdea(models.Model):
    title = models.CharField(max_length=255)
    target_age = models.CharField(max_length=10, choices=AGE_CHOICES)
    target_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.CharField(max_length=1000)
    product_link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    #hobby flags
    tech_flag = models.BooleanField()
    fitness_flag = models.BooleanField()
    fashion_flag = models.BooleanField()
    travel_flag = models.BooleanField()
    music_flag = models.BooleanField()
    home_flag = models.BooleanField()

    upvote = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(max_length=255, unique=True)

    # class Meta:
    #     ordering = ['created']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.gift', args=[self.slug])

class GifteeDataForm(forms.Form):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=10, choices=AGE_CHOICES)
    #price range
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES)
    #####
    tags = models.CharField(max_length=255, blank=True, null=True)
    upvote = models.IntegerField(default=0)
    #hobby category search terms
    sports_flag = models.BooleanField()
    fashion_flag = models.BooleanField()
    active_flag = models.BooleanField()
    tech_flag = models.BooleanField()
    music_flag = models.BooleanField()
    games_flag = models.BooleanField()
