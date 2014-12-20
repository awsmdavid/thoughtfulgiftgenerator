from django.db import models
from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm
 
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class GiftIdea(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    target_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
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
    
    # @property
    # def rank(self):
    #     # get giftIdea Rank
    #     return self._rank

    # @rank.setter
    # def rank(self, value):
    #     # set giftIdea Rank
    #     self._rank = value

    # def calculate_rank(self, GifteeDataForm):
    #     score = 0
    #     if self.tech_flag==GifteeDataForm.tech_flag:
    #         score +=1
    #     self.rank(score)
    #     return self.rank


    # class Meta:
    #     ordering = ['created']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.gift', args=[self.slug])

class GifteeDataForm(forms.Form):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=10)
    tags = models.CharField(max_length=255, blank=True, null=True)
    upvote = models.IntegerField(default=0)
    #hobby category search terms
    sports_flag = models.BooleanField()
    fashion_flag = models.BooleanField()
    active_flag = models.BooleanField()
    tech_flag = models.BooleanField()
    music_flag = models.BooleanField()
    games_flag = models.BooleanField()
    #price range
    price = models.CharField(max_length=10)