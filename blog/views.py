from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('is_done','created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def is_done(request,pk):
    task=get_object_or_404(Post, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(post_list)



