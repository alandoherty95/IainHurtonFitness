from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm


def all_blogposts(request):
    """ A view showing all posts in our blog """
    posts = BlogPost.objects.all().order_by('-date_created')

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def blogpost_detail(request, post_id):
    """ A view showing individual posts in our blog """
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blogpost_detail.html', context)


@login_required
def add_blogpost(request):
    """ Adds a post to our blog """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the admin can perform this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(
                request, f'Successfully added {blogpost.title} to our blog!')
            return redirect(reverse('blogpost_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           'Failed to add blog post. \
                           Please check if the form is valid.')
    else:
        print(request.method)
        form = BlogForm()

    template = 'blog/add_blogpost.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blogpost(request, post_id):
    """ Edit a blogpost """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the admin can perform this action.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {post.title}!')
            return redirect(reverse('blogpost_detail', args=[post.id]))
        else:
            messages.error(request, f'Failed to update {post.title}.\
                                     Please check if the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are currently editing {post.title}')

    template = 'blog/edit_blogpost.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_blogpost(request, post_id):
    """ Deletes a post from our blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    messages.success(request, f'{post.title} was successfully deleted!')
    return redirect(reverse('all_blogposts'))