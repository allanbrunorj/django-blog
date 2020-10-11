from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    x = [1,2,3,4,5]
    return render(request, 'blog/post_list.html', {'posts': posts, 'x': x})
