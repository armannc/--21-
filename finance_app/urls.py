# finance_app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('finance_app.expenses.urls', 'expenses'), namespace='expenses')),
]
