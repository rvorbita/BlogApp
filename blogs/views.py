from django.shortcuts import render,redirect,get_object_or_404

from . models import BlogPost
from . forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.s
def index(request):

    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts }
    return render(request, "blogs/index.html", context)


@login_required
def new_blog(request):
    """Add new Blog"""

    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)

        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            form.save()
            return redirect("blogs:index")
    
    context = {'form': form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def edit_blog(request, blog_id):
    """edit existing blog"""

    # blogpost = BlogPost.objects.get(id=blog_id)
    blogpost = get_object_or_404(BlogPost, id=blog_id)
    #check for post owner raise 404 if not the owner.
    check_blog_owner(blogpost.owner, request.user)

    if request.method != "POST":
        form = BlogForm(instance=blogpost)
    else:
        form = BlogForm(instance=blogpost, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {'blogpost': blogpost, 'form': form }
    return render(request, "blogs/edit_blog.html", context)

@login_required
def delete_blog(request, blog_id):
    """delete existing blog"""

    blogpost = BlogPost.objects.get(id=blog_id)
    
    #check for post owner raise 404 if not the owner.
    check_blog_owner(blogpost.owner, request.user)
    
    if request.method == "POST":
        blogpost.delete()
        return redirect("blogs:index")
        
    context = {'blogpost': blogpost}
    return render(request, "blogs/delete_blog.html", context)


def check_blog_owner(owner, request):

    if owner != request:
        raise Http404