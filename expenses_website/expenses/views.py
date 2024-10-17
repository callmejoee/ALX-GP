from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Category, Expense
from userpreferences.models import UserPreference
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from django.http import JsonResponse

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def index(request):
    expense=Expense.objects.filter(owner=request.user)
    paginator = Paginator(expense, 5)
    page_number=request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = ""
    context = {
        'expenses': expense,
        'page_obj': page_obj,
        'currency': currency
    }
    categories = Category.objects.all()
    return render(request, 'expenses/index.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def add_expense(request):
    if request.method == "POST":
        amount = request.POST['amount']
        date = request.POST['date']
        category = request.POST['category']
        description = request.POST['description']

        Expense.objects.create(amount=amount, date=date, category=category, description=description, owner=request.user)
        messages.success(request, "Expense saved successfully")
        return redirect("expenses")

    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = ""

    categories = Category.objects.all()
    context = {
        'categories':categories,
        'currency': currency,
    }
    return render(request, 'expenses/add_expenses.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = ""

    if request.method == "POST":
        expense.amount = request.POST.get('amount', expense.amount)
        expense.date = request.POST.get('date', expense.date)
        expense.category = request.POST.get('category', expense.category)
        expense.description = request.POST.get('description', expense.description)
        expense.save()

        messages.success(request, "Expense updated successfully")
        return redirect("expenses")

    context = {
        'expense': expense,
        'categories': categories,
        'currency': currency,
        'values': {
            'amount': expense.amount,
            'date': expense.date,
            'category': expense.category,
            'description': expense.description
        }
    }

    return render(request, 'expenses/edit-expense.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def delete_expense(request, id):
    expense=Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, "Expense Removed")
    return redirect('expenses')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def expense_category_sumarry(request):
    todays_date= datetime.date.today()
    last_quarter = todays_date - datetime.timedelta(30)
    expenses=Expense.objects.filter(date__gte=last_quarter, date__lte=todays_date, owner=request.user)

    final_rep = {}
    
    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount

        return amount

    for x in expenses:
        for y in category_list:
            final_rep[y] = get_expense_category_amount(y)
    return JsonResponse({'expense_category_data': final_rep}, safe=False)


def statsView(request):
    return render(request, 'expenses/stats.html')


def home(request):
    return render(request, 'partials/home.html')


def prices(request):
    return render(request, 'partials/prices.html')


def features(request):
    return render(request, 'partials/features.html')

