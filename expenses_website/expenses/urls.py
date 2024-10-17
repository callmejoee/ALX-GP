from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('', views.index, name="index"),
    path('add-expense', views.add_expense, name="add-expense"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense_edit"),
    path('home', views.home, name="home"),
    path('prices', views.prices, name="prices"),
    path('features', views.features, name="features"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('stats', views.statsView, name="stats"),
    path('expense_category_sumarry', views.expense_category_sumarry, name="expense_category_sumarry")

]