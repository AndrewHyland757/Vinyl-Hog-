from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def test(request):
    return render(request, "errors/404_test.html")


def footer_shipping(request):
    return render(request, 'footer_templates/shipping.html')

def footer_returns(request):
    return render(request, 'footer_templates/returns.html')

def footer_our_story(request):
    return render(request, 'footer_templates/our_story.html')

def footer_planet_vinylhog(request):
    return render(request, 'footer_templates/planet_vinylhog.html')

