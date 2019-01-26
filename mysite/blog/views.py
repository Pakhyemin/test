from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list (request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
def index (request):
    return  render(request, 'blog/index.html', {})
def post_detail (request, pk):
    p = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'p':p})