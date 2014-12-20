from django.shortcuts import render, get_object_or_404
from blog.models import GiftIdea, GifteeDataForm
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
	return render(request, 'blog/index.html')

# 	return render(request, 'blog/results.html')
def submit(request):
	return render(request, 'blog/index.html')

def results(request):
    if request.GET: # If the form has been submitted...
    	gifteeDataForm = GifteeDataForm
        gifteeDataForm.gender = request.GET.get('gender')
    	gifteeDataForm.age = request.GET.get('age')
        gifteeDataForm.price = request.GET.get('price')
    	gifteeDataForm.tech_flag = request.GET.get('tech_flag')
    	gifteeDataForm.fitness_flag = request.GET.get('fitness_flag')
    	gifteeDataForm.travel_flag = request.GET.get('travel_flag')
    	gifteeDataForm.fashion_flag = request.GET.get('fashion_flag')
    	gifteeDataForm.music_flag = request.GET.get('music_flag')
        gifteeDataForm.home_flag = request.GET.get('home_flag')
        # fix this
        gift_idea_result = GiftIdea.objects.filter(Q(tech_flag=gifteeDataForm.tech_flag) | Q(fitness_flag=gifteeDataForm.fitness_flag) | Q(travel_flag=gifteeDataForm.travel_flag) | Q(fashion_flag=gifteeDataForm.fashion_flag) | Q(music_flag=gifteeDataForm.music_flag)).filter(published=True, target_gender=gifteeDataForm.gender).order_by('-upvote')[:1]
        # gift_idea_result = GiftIdea.objects.filter(published=True, target_gender=gifteeDataForm.gender, Q(tech_flag=gifteeDataForm.tech_flag) | Q(fitness_flag=gifteeDataForm.fitness_flag) | Q(travel_flag=gifteeDataForm.travel_flag) | Q(fashion_flag=gifteeDataForm.fashion_flag) | Q(music_flag=gifteeDataForm.music_flag)).order_by('-upvote')[:1]
        # for GiftIdea.object in gift_idea_result:
            # GiftIdea.object.match_rank = GiftIdea.object.calculate_rank(gifteeDataForm)
        # TODO: add age, price, and categories
        gift_idea_secondary_results = GiftIdea.objects.filter(published=True, target_gender=gifteeDataForm.gender).order_by('-upvote')[1:]
        # gift_idea_result = GiftIdea.objects.filter(Q(tags__icontains = search_term) | Q(description__icontains= search_term)).order_by('-likes')[:5]
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results, 'gifteeDataForm': gifteeDataForm}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def random(request):
    if request.GET: # If the form has been submitted...
        gift_idea_result = GiftIdea.objects.filter(published=True).order_by('-upvote')[:1]
        gift_idea_secondary_results = GiftIdea.objects.filter(published=True).order_by('-upvote')[1:]
        # gift_idea_result = GiftIdea.objects.filter(Q(tags__icontains = search_term) | Q(description__icontains= search_term)).order_by('-likes')[:5]
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')


def gift(request):
    # get the Post object
    giftIdea = get_object_or_404(GiftIdea, slug=slug)
    # widget_posts = Post.objects.filter(published=True).exclude(slug=slug).order_by('?')[:5]
    # now return the rendered template
    return render(request)