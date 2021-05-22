from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


        # if we want particular fields for the form we make a list like fields = ['customer', 'product']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'



