from django.urls import path
from . import views

urlpatterns = [
    path('', views.income, name="income"),
    path('add-income', views.add_income, name="add-income"),
    path('edit-income/<int:id>', views.income_edit, name="income_edit"),
    path('income-delete/<int:id>', views.delete_income, name="income-delete"),
    path('income_source_sumarry', views.income_source_sumarry, name="income_source_sumarry"),
    path('income-stats', views.statsView, name="income-stats"),

]