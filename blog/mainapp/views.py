from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {}) #index.html будет отрисовыватся в билде


def category_detail(request, id):
    return render(request, 'index.html', {})


def post_detail(request, id):
    return render(request, 'index.html', {})
