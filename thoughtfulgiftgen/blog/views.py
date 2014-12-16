from django.shortcuts import render, get_object_or_404
from blog.models import GifteeDataForm, GiftIdea
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'blog/index.html')

# 	return render(request, 'blog/results.html')
def submit(request):
	return render(request, 'blog/index.html')

def results(request):
    if request.GET: # If the form has been submitted...
    	gender = request.GET.get('gender')
    	age = request.GET.get('age')
    	priceMin = request.GET.get('priceMin')
    	priceMax = request.GET.get('priceMax')
    	tech_flag = request.GET.get('tech_flag')
    	sports_flag = request.GET.get('sports_flag')
    	travel_flag = request.GET.get('travel_flag')
    	fashion_flag = request.GET.get('fashion_flag')
    	music_flag = request.GET.get('music_flag')
        gift_idea_result = GiftIdea.objects.filter(published=True)
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gender': gender, 'age': age, 'priceMin': priceMin, 'priceMax':priceMax, 'tech_flag':tech_flag, 'sports_flag':sports_flag, 'travel_flag':travel_flag, 'fashion_flag':fashion_flag, 'music_flag':music_flag}) # Redirect after POST    # if request.POST: # If the form has been submitted...
	   #  inputData = GifteeDataForm(request.POST)
	   #  return render(request, 'blog/results.html', {'inputData': inputData}) # Redirect after POST
    return render(request, 'blog/index.html')

def gift(request):
    # get the Post object
    giftIdea = get_object_or_404(GiftIDea, slug=slug)
    # widget_posts = Post.objects.filter(published=True).exclude(slug=slug).order_by('?')[:5]
    # now return the rendered template
    return render(request)