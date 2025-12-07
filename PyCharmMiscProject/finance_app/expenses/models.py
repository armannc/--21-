from django.db import models
class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    big_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {int(self.amount)} ₸"

class BigExpense(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="big_expenses")
    limit = models.FloatField()

    def is_big(self):
        return self.expense.amount >= self.limit

    def __str__(self):
        return f"{self.expense.name} (limit: {int(self.limit)})"
