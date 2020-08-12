from django.shortcuts import render, redirect

# Create your views here.


def page(request):
    return render(request, 'index.html', {})
