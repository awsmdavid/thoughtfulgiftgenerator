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
        gifteeDataForm.price_range = request.GET.get('price_range')
    	gifteeDataForm.tech_flag = request.GET.get('tech_flag')
    	gifteeDataForm.fitness_flag = request.GET.get('fitness_flag')
    	gifteeDataForm.travel_flag = request.GET.get('travel_flag')
    	gifteeDataForm.fashion_flag = request.GET.get('fashion_flag')
    	gifteeDataForm.music_flag = request.GET.get('music_flag')
        gifteeDataForm.home_flag = request.GET.get('home_flag')
        # if gender was answerd:
        if request.GET.get('gender'):
            if request.GET.get('age'):
                if request.GET.get('price_range'):
                    gift_idea_result = GiftIdea.objects.filter(
                        Q(tech_flag=gifteeDataForm.tech_flag) | 
                        Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                        Q(travel_flag=gifteeDataForm.travel_flag) | 
                        Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                        Q(music_flag=gifteeDataForm.music_flag) |
                        Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender, target_age=gifteeDataForm.age, price_range=gifteeDataForm.price_range).order_by('-upvote')
                else:
                    gift_idea_result = GiftIdea.objects.filter(
                        Q(tech_flag=gifteeDataForm.tech_flag) | 
                        Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                        Q(travel_flag=gifteeDataForm.travel_flag) | 
                        Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                        Q(music_flag=gifteeDataForm.music_flag) |
                        Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender, target_age=gifteeDataForm.age).order_by('-upvote')
            else:
                gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender).order_by('-upvote')
        # if age was answerd (but gender was not):
        elif request.GET.get('age'):
            if request.GET.get('price_range'):
                gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_age=gifteeDataForm.age, price_range = gifteeDataForm.price_range).order_by('-upvote')
            else:
                gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_age=gifteeDataForm.age).order_by('-upvote')
        # if price was answerd (but gender and age were not):
        elif request.GET.get('price_range'):
            gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, price_range = gifteeDataForm.price_range).order_by('-upvote')
        # if nothing was answerd (perhaps a category):
        else:
            gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True).order_by('-upvote')

        gift_idea_secondary_results = gift_idea_result[1:4]
        gift_idea_result = gift_idea_result[:1]
        
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def random(request):
    if request.GET: # TODO: eliminate duplicates
        gift_idea_results = GiftIdea.objects.filter(published=True).order_by('?')
        gift_idea_secondary_results = gift_idea_results[1:4]
        gift_idea_result = gift_idea_results[:1]
        
        # slugs_to_exclude = [giftIdea.title for giftIdea in gift_idea_result] 

        # generate random with more scalable method since order_by('?')[:X] does not scale well?
        # last = GiftIdea.objects.count() - 1
        # index1 = randint(0, last)
        # index2 = randint(0, last - 1)
        # if index2 == index1: index2 = last
        # MyObj1 = MyModel.objects.all()[index1]
        # MyObj2 = MyModel.objects.all()[index2]

        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def gift(request, slug):
    # get the Post object
    gift = get_object_or_404(GiftIdea, slug=slug)
    # now return the rendered template
    return render(request, 'blog/gift.html', { 'gift': gift}) # Redirect after POST    # if request.POST: # If the form has been submitted...
