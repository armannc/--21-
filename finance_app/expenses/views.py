# finance_app/expenses/views.py
from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum

def add_expense(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        big_info = request.POST.get("big_info")

        if name and amount:
            Expense.objects.create(
                name=name,
                amount=float(amount),
                big_info=big_info
            )
            return redirect("expenses:expense_list")

    categories = ["Food", "Transport", "Entertainment", "Health", "Other"]
    return render(request, "expenses/add.html", {"categories": categories})

def expense_list(request):
    expenses = Expense.objects.all().order_by("-created_at")
    return render(request, "expenses/list.html", {"expenses": expenses})

def stats(request):
    data = Expense.objects.values("name").annotate(total_amount=Sum("amount"))
    total_sum = Expense.objects.aggregate(total_sum=Sum("amount"))["total_sum"]
    return render(request, "expenses/stats.html", {"data": data, "total_sum": total_sum})

def home(request):
    total_expenses = Expense.objects.count()

    last_exp = Expense.objects.order_by("-created_at").first()

    context = {
        "total_expenses": total_expenses,
        "last_expense": last_exp.amount if last_exp else 0,
    }

    return render(request, "expenses/home.html", context)