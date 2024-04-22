from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    print('blog1')
    return render(
        request,
        'blog/index.html'
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )
