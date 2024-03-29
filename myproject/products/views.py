from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def add_product(request):
    # Ваша логіка додавання товару
    pass
