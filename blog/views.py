from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


def page_post(request, post_id):
    post = Post.objects.get(id = post_id)

    context = {
        "post": post,
    }
    return render(
        "page_post.html", context
    )