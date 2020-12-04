from django.shortcuts import render, redirect
from blogs.forms import PostForm
from blogs.models import Post


def home(request):
    post = Post.objects.all()

    data = {
        'posts': post
    }

    return render(request, template_name='blogs/home.html', context=data)


def about(request):
    return render(request, template_name='blogs/about.html')


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-url')

    data = {
        'form': form
    }
    return render(request, template_name='blogs/createPost.html', context=data)

# Username
# title
# description
# image
# like,share,comment
