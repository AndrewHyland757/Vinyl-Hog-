from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """
    Display the user's profile page.
    Includes shipping info and order history.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
        "on_profile_page": True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Renders the details of a specific order.
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = "profiles/profile_order.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
