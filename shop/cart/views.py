from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from . cart import Cart
from . forms import CartAddProductForm
from django.views.decorators.http import require_POST


@require_POST
def cart_add():
  ...