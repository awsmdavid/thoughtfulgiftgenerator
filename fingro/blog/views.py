from django.shortcuts import render, get_object_or_404
from blog.models import GifteeDataForm
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'blog/index.html')

# 	return render(request, 'blog/results.html')
def submit(request):
	return render(request, 'blog/index.html')

def post(request, slug):
    # get the Post object
    posts = Post.objects.filter(published=True)
    #return post and slug
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'posts':posts, 'current_slug':slug})

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
        return render(request, 'blog/results.html', { 'gender': gender, 'age': age, 'priceMin': priceMin, 'priceMax':priceMax, 'tech_flag':tech_flag, 'sports_flag':sports_flag, 'travel_flag':travel_flag, 'fashion_flag':fashion_flag, 'music_flag':music_flag}) # Redirect after POST    # if request.POST: # If the form has been submitted...
	   #  inputData = GifteeDataForm(request.POST)
	   #  return render(request, 'blog/results.html', {'inputData': inputData}) # Redirect after POST
    return render(request, 'blog/index.html')

# def submit(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = UserSubmittedPost(request.POST)
#         # if fileType is youtube then parse the id and convert to embed
#         if (request.POST.get('fileType') == "Youtube") & form.is_valid():
#             instance = form.save(commit=False)
#             url_data = urlparse.urlparse(request.POST.get('content'))
#             query = urlparse.parse_qs(url_data.query)
#             videoId = query["v"][0]
#             instance.content = "http://youtube.com/embed/" + videoId
#             instance.save()
#             return HttpResponseRedirect('/submit/') # Redirect after POST

#         if form.is_valid(): # All validation rules pass
#             # save form
#             form.save()
#             #TODO: change redirect to submit but with message
#             return render(request, 'blog/submit.html', {'message': "Thanks for your submission!"}) # Redirect after POST
#     else:
#         form = UserSubmittedPost() # An unbound form

#     return render(request, 'blog/submit.html', {'form': form, 'message': "Submit a post!"})