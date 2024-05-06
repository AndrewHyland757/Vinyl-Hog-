from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import views
from products.models import Album
from .models import RecommendationPost, Author
from .forms import RecommendationPostForm
from django.contrib.auth.decorators import login_required


# Create your views here.

     
def posts(request):
    """
    View to render all the post articles.
    """ 
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
    """ 
    View to view and manage all post articles.
    """

    posts = RecommendationPost.objects.all()
    sub_title = "All Posts"

    template = 'blog/blog_post_management.html'
    context = {
        "posts": posts
        
    }

    return render(request, template, context)





@login_required
def add_post(request):
    """ 
    View to add an blog post article.
    """


    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    user = request.user
    author = get_object_or_404(Author, user=user)

    if request.method == 'POST':
        form = RecommendationPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # Populate the booking instance customer_name field
            post.user = user
            post.author = author

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
        "author": author,
    }

    return render(request, template, context)



@login_required
def add_author(request):
    """ 
    View to add an author name.
    """
    
        
    template = 'blog/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)