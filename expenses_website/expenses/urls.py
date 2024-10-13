from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-expense', views.add_expense, name="add_expenses"),
    path('home', views.home, name="home"),
    path('prices', views.prices, name="prices"),
    path('features', views.features, name="features")

]