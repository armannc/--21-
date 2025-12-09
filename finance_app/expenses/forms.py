from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'big_info']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Мысалы: Тамақ'}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'step':'0.01'}),
        }
