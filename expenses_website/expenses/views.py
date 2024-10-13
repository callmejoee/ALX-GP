from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'expenses/index.html')

def home(request):
    return render(request, 'partials/home.html')

def prices(request):
    return render(request, 'partials/prices.html')


def features(request):
    return render(request, 'partials/features.html')


def add_expense(request):
    return render(request, 'expenses/add_expenses.html')
