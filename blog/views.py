from django.shortcuts import render
from blog.models import Post, Author

def info_list(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    context = {
        'posts_list': posts,
        'authors_list': authors
    }
    return render(request, 'info_list.html', context=context)