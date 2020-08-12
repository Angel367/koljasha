from django.shortcuts import render, redirect

# Create your views here.


def main_page(request):
    return render(request, 'index.html', {})


def handler404(request, exception=0):
    return render(request, 'index.html', {})
