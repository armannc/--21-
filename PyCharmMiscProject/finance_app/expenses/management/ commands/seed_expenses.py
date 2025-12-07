from django.core.management.base import BaseCommand
from expenses.models import Expense

class Command(BaseCommand):
    help = 'Seed default expenses'

    def handle(self, *args, **kwargs):
        defaults = [
            ("Тамақ", 60000),
            ("Жол ақысы", 15000),
            ("Коммуналка", 20000),
        ]
        for name, amount in defaults:
            if not Expense.objects.filter(name=name).exists():
                Expense.objects.create(name=name, amount=amount)
        self.stdout.write(self.style.SUCCESS('Default expenses added.'))
