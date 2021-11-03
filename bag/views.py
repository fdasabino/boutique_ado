from django.shortcuts import render

# Create your views here.


def views_bag(request):
    """
    A view to return the shopping bag content
    """
    return render(request, 'bag.html')
