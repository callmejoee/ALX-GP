from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/authentication/login")
def index(request):
    expense=Expense.objects.filter(owner=request.user)
    paginator = Paginator(expense, 5)
    page_number=request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'expenses': expense,
        'page_obj': page_obj
    }
    categories = Category.objects.all()
    return render(request, 'expenses/index.html', context)


def add_expense(request):
    if request.method == "POST":
        amount = request.POST['amount']
        date = request.POST['date']
        category = request.POST['category']
        description = request.POST['description']

        Expense.objects.create(amount=amount, date=date, category=category, description=description, owner=request.user)
        messages.success(request, "Expense saved successfully")
        return redirect("expenses")

    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'expenses/add_expenses.html', context)


def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()

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
        'values': {
            'amount': expense.amount,
            'date': expense.date,
            'category': expense.category,
            'description': expense.description
        }
    }

    return render(request, 'expenses/edit-expense.html', context)

def delete_expense(request, id):
    expense=Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, "Expense Removed")
    return redirect('expenses')





def home(request):
    return render(request, 'partials/home.html')


def prices(request):
    return render(request, 'partials/prices.html')


def features(request):
    return render(request, 'partials/features.html')

