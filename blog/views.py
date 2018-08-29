from django.shortcuts import render, get_object_or_404
# --------------------------------------------------------------------------------------------
# Here we are saying that Django go to the same directory ("." denotes) and look into def Post 
# and get usefull instruction from there
from .models import Post
#---------------------------------------------------------------------------------------------
# just want to get all the library of time zone for python
from django.utils import timezone
#---------------------------------------------------------------------------------------------
# Add this import inorder to let the add form and edit form to work
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
	#------- order the Posts according to date it was published and store it to variable "posts" as QuerySet
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#------- something the template (in this case the post_list.html) can use 
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

#---- Code below is for new blog onced clicked the + button
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

#---- Code below is for editing routines in the blog once clicked the pencil button

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method =="POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
	