from django.shortcuts import render, redirect

# Create your views here.


def main_page(request):
    return render(request, 'index.html', {})


def main_redirect(request):
    return redirect('/main/')
