from django.shortcuts import render, get_object_or_404
from blog.models import GiftIdea, GifteeDataForm
# from django.http import HttpResponseRedirect
from django.db.models import Q
import operator

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
        
        key_filter_args=[]
        category_filter_args=[]

        if gifteeDataForm.gender:
            key_filter_args.append( Q(**{'target_gender':gifteeDataForm.gender} ) )
        if gifteeDataForm.age:
            key_filter_args.append( Q(**{'target_age':gifteeDataForm.age} ) )
        if gifteeDataForm.price_range:
            key_filter_args.append( Q(**{'price_range':gifteeDataForm.price_range} ) )

        if gifteeDataForm.tech_flag:
            category_filter_args.append( Q(**{'tech_flag':True} ) )
        if gifteeDataForm.fitness_flag:
            category_filter_args.append( Q(**{'fitness_flag':True} ) )
        if gifteeDataForm.travel_flag:
            category_filter_args.append( Q(**{'travel_flag':True} ) )
        if gifteeDataForm.fashion_flag:
            category_filter_args.append( Q(**{'fashion_flag':True} ) )
        if gifteeDataForm.music_flag:
            category_filter_args.append( Q(**{'music_flag':True} ) )
        if gifteeDataForm.home_flag:
            category_filter_args.append( Q(**{'home_flag':True} ) )

        # apply filter criteria for demographic data
        if key_filter_args:
            gift_idea_results = GiftIdea.objects.filter(reduce(operator.and_, key_filter_args))
        # apply filter criteria for category data
        if category_filter_args:
            gift_idea_results = GiftIdea.objects.filter(reduce(operator.or_, category_filter_args))

        try:
            gift_idea_result = gift_idea_results[0]
            slug_to_exclude = gift_idea_result.slug
            gift_idea_secondary_results = gift_idea_results.exclude(slug=slug_to_exclude).order_by('?')[:3]
        except:
            try:
                if GiftIdea.objects.filter(reduce(operator.and_, key_filter_args))[0]:
                    #TODO: add finer granularity in case nothing hits all three categories
                    gift_idea_results = GiftIdea.objects.filter(reduce(operator.and_, key_filter_args))
                elif GiftIdea.objects.filter(reduce(operator.and_, category_filter_args))[0]:
                    gift_idea_results = GiftIdea.objects.filter(reduce(operator.or_, category_filter_args))
                else:
                    gift_idea_results = GiftIdea.objects.filter(published=True).order_by('?')
            except:
                gift_idea_results = GiftIdea.objects.filter(published=True).order_by('?')

            gift_idea_result = gift_idea_results[0]
            slug_to_exclude = gift_idea_result.slug
            gift_idea_secondary_results = GiftIdea.objects.exclude(slug=slug_to_exclude).order_by('?')[:3]

        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def random(request):
    if request.GET: # TODO: eliminate duplicates
        gift_idea_result = GiftIdea.objects.filter(published=True).order_by('?')[0]
        slug_to_exclude = gift_idea_result.slug
        gift_idea_secondary_results = GiftIdea.objects.filter(published=True).exclude(slug=slug_to_exclude).order_by('?')[:3]
        
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def gift(request, slug):
    # get the Post object
    gift = get_object_or_404(GiftIdea, slug=slug)
    # now return the rendered template
    return render(request, 'blog/gift.html', { 'gift': gift}) # Redirect after POST    # if request.POST: # If the form has been submitted...
