from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import forms


@login_required
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = forms.SignupForm()

    return render(request, "registration/signup.html", {"form": form})
