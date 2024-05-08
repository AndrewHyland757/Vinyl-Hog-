from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from . import views
from products.models import Album
from .models import RecommendationPost
from .forms import RecommendationPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def posts(request):
    '''
    View to render all the post articles.
    '''
    posts = RecommendationPost.objects.all()
    posts_by_date = RecommendationPost.objects.all().order_by('-created_on')

    context = {
        "posts": posts,
    }

    return render(request, 'blog/posts.html', context)


def post(request, post_id):
    '''
    View to render an individual article.
    '''
    post = get_object_or_404(RecommendationPost, id=post_id)

    context = {
        "post": post,
    }

    return render(request, 'blog/post.html', context)


@login_required
def blog_post_management(request):
    '''
    View to view and manage all post articles.
    '''
    posts = RecommendationPost.objects.all()
    sub_title = "All Posts"

    template = 'blog/blog_post_management.html'
    context = {
        "posts": posts
    }

    return render(request, template, context)


@login_required
def add_post(request):
    '''
    View to add a post article.
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    user = request.user

    if request.method == 'POST':
        form = RecommendationPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # Populate the booking instance customer_name field
            post.user = user
            post = form.save()
            messages.success(request, 'Successfully added post!')
            '''
            return redirect(reverse('product_detail', args=[product.id]))
            '''
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = RecommendationPostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    '''
    View to edit a post article.
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(RecommendationPost, pk=post_id)

    if request.method == 'POST':
        form = RecommendationPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = RecommendationPostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    '''
    View to delete a post article.
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(RecommendationPost, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog-post-management'))
