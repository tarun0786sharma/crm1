from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .filters import OrderFilter


def home(request):
    lastorders = Order.objects.all().order_by('-date_created')[:5]
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count
    out_for_delivery = orders.filter(status='Out for delivery').count
    pending = orders.filter(status='Pending').count
    context = {'orders': orders, 'customers': customers, 'delivered': delivered, 'total_customers': total_customers,
               'pending': pending, 'total_orders': total_orders, 'out_for_delivery': out_for_delivery,
               'lastorders': lastorders, }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product = Product.objects.all
    context = {'product': product}

    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)




def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=8)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)



def updateOrder(request, pk):
    task = Order.objects.get(id=pk)
    form = OrderForm(instance=task)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'task': task}
    return render(request, 'accounts/update_order.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)


def updateCustomer(request, pk):
    task = Customer.objects.get(id=pk)
    form = CustomerForm(instance=task)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'task': task}
    return render(request, 'accounts/update_customer.html', context)


def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'customer': customer}
    return render(request, 'accounts/delete_customer.html', context)


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'accounts/create_product.html', context)


def updateProduct(request, pk):
    task = Product.objects.get(id=pk)
    form = ProductForm(instance=task)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form, 'task': task}
    return render(request, 'accounts/update_customer.html', context)


def deleteProduct(request, pk):
    task = Product.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('products')
    context = {'task': task}
    return render(request, 'accounts/delete_product.html', context)



def createTag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'accounts/create_tag.html', context)
