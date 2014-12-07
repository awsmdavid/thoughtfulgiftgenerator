from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    # render index
    return render(request, 'blog/index.html')

def submit(request, gender, age, hobbies):
	# if request.method == 'POST': # If the form has been submitted...
	# 	if form.is_valid(): # All validation rules pass
	# 		form.save()

	# userdata = get_object_or_404(UserData, gender=gender, age=age, hobbies=hobbies)
	return render(request, 'blog/results.html')
	# return render(request, 'blog/results.html', {'userdata': userdata})

def post(request, slug):
    # get the Post object
    posts = Post.objects.filter(published=True)

    #return post and slug
    post = get_object_or_404(Post, slug=slug)

    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'posts':posts, 'current_slug':slug})

def results(request):
	return render(request, 'blog/results.html')

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