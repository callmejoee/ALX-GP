from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
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
