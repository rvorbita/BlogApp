from django.shortcuts import render,redirect

from . models import BlogPost
from . forms import BlogForm

# Create your views here.
def index(request):

    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts }
    return render(request, "blogs/index.html", context)



def new_blog(request):
    """Add new Blog"""

    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    
    context = {'form': form}
    return render(request, "blogs/new_blog.html", context)



def edit_blog(request, blog_id):
    """edit existing blog"""

    blogpost = BlogPost.objects.get(id=blog_id)


    if request.method != "POST":
        form = BlogForm(instance=blogpost)
    else:
        form = BlogForm(instance=blogpost, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {'blogpost': blogpost, 'form': form }
    return render(request, "blogs/edit_blog.html", context)


def delete_blog(request, blog_id):
    """delete existing blog"""

    blogpost = BlogPost.objects.get(id=blog_id)
    
    if request.method == "POST":
        blogpost.delete()
        return redirect("blogs:index")
        
    context = {'blogpost': blogpost}
    return render(request, "blogs/delete_blog.html", context)