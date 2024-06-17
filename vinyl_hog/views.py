from django.shortcuts import render


def handler404(request, exception):
    """ 
    Error Handler 404 - Page Not Found 
    """
    return render(request, "errors/404.html", status=404)


def footer_shipping(request):
    """ 
    Renders footer shipping info page
    """
    return render(request, "footer_templates/shipping.html")


def footer_returns(request):
    """ 
    Renders footer returns info page
    """
    return render(request, "footer_templates/returns.html")


def footer_our_story(request):
    """ 
    Renders footer abput page
    """
    return render(request, "footer_templates/our_story.html")


def footer_planet_vinylhog(request):
    """ 
    Renders footer planet vinyl hog page
    """
    return render(request, "footer_templates/planet_vinylhog.html")
