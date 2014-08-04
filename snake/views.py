from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def snake(request):
    return render(request, 'snake.html')

