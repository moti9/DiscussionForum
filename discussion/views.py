from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Vote
from django.core.paginator import Paginator
# Create your views here.


@login_required
def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # form.save()
            messages.success(request, "Post created successfully!!",
                             extra_tags='alert alert-success alert-dismissible fade show')
            # return redirect('discussion:createpost')
        else:
            messages.error(request, "Oops someting is missing,please try angain!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    context = {
        'form': form,
    }
    return render(request, 'discussion/create.html', context)


def home(request):
    posts = Post.objects.all()
    search_term = ''
    try:
        if 'name' in request.GET:
            posts = posts.order_by('title')

        if 'date' in request.GET:
            posts = posts.order_by('pub_date')

        if 'vote' in request.GET:
            posts = posts.order_by('-votes')

        if 'search' in request.GET:
            search_term = request.GET['search']
            posts = posts.filter(text__icontains=search_term)
    except:
        pass
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    dict = request.GET.copy()
    params = dict.pop('page', True) and dict.urlencode()
    return render(request, 'discussion/home.html', {'posts': posts, 'params': params, 'search_term': search_term})


@login_required
def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        user = request.user

        try:
            if Vote.objects.filter(post=post, voter=user).exists():
                # post.votes -= 1
                # vote = Vote.objects.filter(post=post, voter=user)
                # vote.delete()
                pass
            else:
                Vote.objects.create(post=post, voter=user)
                post.votes += 1
                post.save()
        except:
            pass
        next = request.POST.get('next', '/')
        return redirect(next)


@login_required
def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        user = request.user
        try:
            if Vote.objects.filter(post=post, voter=user).exists():
                # post.votes += 1
                # vote = Vote.objects.filter(post=post, voter=user)
                # vote.delete()
                pass
            else:
                Vote.objects.create(post=post, voter=user)
                post.votes -= 1
                post.save()
        except:
            pass
        next = request.POST.get('next', '/')
        return redirect(next)


@login_required
def userposts(request, pk):
    posts = Post.objects.filter(author__id=pk).order_by('-pub_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    dict = request.GET.copy()
    params = dict.pop('page', True) and dict.urlencode()
    author = User.objects.get(pk=pk)
    return render(request, 'discussion/userposts.html', {'posts': posts, 'author': author, 'params': params})


@login_required
def post(request, pk):
    post = Post.objects.filter(id=pk)
    return render(request, 'discussion/detail.html', {'post': post})
