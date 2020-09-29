from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    """Register User"""

    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("blogs:index")
    
    context = {'form': form}
    return render(request, "registration/register.html", context)
