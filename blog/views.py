from django.shortcuts import render, get_object_or_404
# --------------------------------------------------------------------------------------------
# Here we are saying that Django go to the same directory ("." denotes) and look into def Post 
# and get usefull instruction from there
from .models import Post
#---------------------------------------------------------------------------------------------
from django.utils import timezone

# Create your views here.
def post_list(request):
	#------- order the Posts according to date it was published and store it to variable "posts" as QuerySet
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#------- something the template (in this case the post_list.html) can use 
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})