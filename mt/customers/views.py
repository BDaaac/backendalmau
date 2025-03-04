from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm



def customer_list(request):
    customers = Customer.objects.all()  # Получаем всех клиентов
    return render(request, 'customers/customers_list.html', {'customers': customers})


def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

# 📌 Добавление клиента
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})

# 📌 Редактирование клиента
def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/edit_customer.html', {'form': form})

# 📌 Удаление клиента
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        customer.delete()
        return redirect('customers_list')
    return render(request, 'customers/delete_customer.html', {'customer': customer})
