from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def memu_view(request):
    return render(request, 'blogapp/menu.html', {'hostport': 'http://127.0.0.1:800'})


# Create your views here.
def main_view(request):
    posts = Post.objects.select_related('user').all().order_by('-create')
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    title = 'Home'
    return render(request, 'blogapp/index.html', context={'posts': posts, 'title': title})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post, 'title': post.name})


@login_required
@csrf_exempt
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            # Добавить в форму текущего пользователя request.user - текущий пользователь
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})


@login_required
@csrf_exempt
def create_post_safe(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            # Добавить в форму текущего пользователя request.user - текущий пользователь
            form.instance.user = request.user
            form.instance.text = form.instance.text.replace('script', '_')
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
