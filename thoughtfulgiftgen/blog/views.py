from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)

    post = get_object_or_404(Post, slug='prologue')

    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'posts': posts, 'current_slug':'prologue'})
 
def post(request, slug):
    # get the Post object
    posts = Post.objects.filter(published=True)

    #return post and slug
    post = get_object_or_404(Post, slug=slug)

    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'posts':posts, 'current_slug':slug})