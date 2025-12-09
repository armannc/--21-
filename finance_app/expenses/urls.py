from django.urls import path
from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.home, name="home"),  # басты бет
    path("add/", views.add_expense, name="add_expense"),
    path("list/", views.expense_list, name="expense_list"),
    path("stats/", views.stats, name="stats"),
]
