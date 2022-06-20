import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import DetailView

def Movie_Detail_View(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html', context={'movie_detail': movie})

def Director_Detail_View(request, id):
    director = Director.objects.get(id=id)
    return render(request, 'director_detail.html', context={'director_detail': director})

def Reviews_Detail_View(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'review_detail.html', context={'review_detail': review})

def index(request):
    description = Movie.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Movies', 'description': description})

    name = Director.objects.order_by('-id')
    return render(request, 'main/index.html', {'name': name})

    text = Review.objects.order_by('-id')
    return render(request, 'main/index.html', {'text': text})
def movies(request):
    error = ''
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            error = 'Error'
    form = MovieForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/movies.html', context)
def directors(request):
    error = ''
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            error = 'Error'
    form = DirectorForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/directors.html', context)

def reviews(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            error = 'Error'
    form = ReviewForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/reviews.html', context)

