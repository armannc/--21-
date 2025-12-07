from django.contrib import admin
from .models import Expense, BigExpense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','name','amount','created_at')
    search_fields = ('name',)

@admin.register(BigExpense)
class BigExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense','limit')
