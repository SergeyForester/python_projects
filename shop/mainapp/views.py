import datetime

import django
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
import mainapp
from mainapp import utils
from mainapp.models import Category, Product, Order, OrderItem, Sort


def main(request):
    categories = Category.objects.all()
    new_products = Product.objects.all().order_by('-date')[:3]
    top_products = Product.objects.all().order_by('-rating')[:6]
    sorts = Sort.objects.all()

    utils.convert_filters()

    try:
        order = Order.objects.get(user=request.session.session_key)
        items = OrderItem.objects.filter(order=order)
        total = sum([item.item.price * item.quantity for item in items])
    except Exception as err:
        total = 0
        print(err)

    lengths = []
    for product in Product.objects.all():
        if not product.length in lengths:
            lengths.append(product.length)

    content = {'categories': categories, 'new_products': new_products,
               'top_products': top_products, 'sorts': sorts, 'lengths': lengths,
               'total': total, "filter_data": utils.convert_filters()}
    return render(request, 'mainapp/index.html', content)


def search(request):
    categories = Category.objects.all()

    # filters = {
    #     key: value.split("-")[0]
    #     for key, value in request.POST.items()
    #     if value and key in ['category', 'sort', 'length']
    # }

    res = Product.objects.all()
    data = request.POST

    print(data)
    for key, value in data.items():
        if key == 'category' and data[key]:
            res.filter(category=Category.objects.get(name=value))
        if key == 'sort' and data[key]:
            res.filter(sort=Sort.objects.get(name=value))
        if key == 'length' and data[key]:
            res.filter(length=value)


    print(res)


    return render(request, 'mainapp/search.html', {'products': res, 'categories': categories})


def cart_remove(request, id):
    order = OrderItem.objects.get(id=id)
    order.item.quantity += order.quantity
    order.item.save()
    order.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", '/'))


def categories(request, category):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category)
    products = Product.objects.filter(category=category)

    content = {'categories': categories, 'products': products, 'category': category}
    return render(request, 'mainapp/category.html', content)


def cart(request):
    try:
        order = Order.objects.get(user=request.session.session_key)
        items = OrderItem.objects.filter(order=order)
        categories = Category.objects.all()
        total = sum([item.item.price * item.quantity for item in items])

        content = {'items': items, 'order': order, 'categories': categories, 'total': total}

    except mainapp.models.Order.DoesNotExist:
        content = {}

    print(content)

    return render(request, 'mainapp/cart.html', content)


def add_to_cart(request):
    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key
    try:
        order = Order.objects.filter(user=session_id).reverse()[:1][0]  # get the last order
    except:
        order = Order.objects.create(user=session_id)

    print(request.POST['product'])

    order_item = OrderItem.objects.filter(order=order, item__id=request.POST['product'])[:1]

    if (Product.objects.get(id=int(request.POST['product'])).quantity - int(request.POST.get('quantity', 1))) >= 0:
        print(order_item)
        if not order_item:
            # create order item
            order_item = OrderItem.objects.create(order=order,
                                                  quantity=int(request.POST.get('quantity', 1)),
                                                  item=Product.objects.get(id=int(request.POST['product'])))
        else:
            order_item = order_item[0]
            order_item.quantity += int(request.POST.get('quantity', 1))

        order_item.item.quantity -= int(request.POST.get('quantity', 1))
        order_item.item.save()

        order_item.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", '/'))


def changeOIQ(request):
    print(request.POST['product'])
    item = get_object_or_404(OrderItem, id=request.POST['product'])

    if item.quantity > int(request.POST['quantity']):  # ex. 7 -> 3 = +4
        item.item.quantity += item.quantity - int(request.POST['quantity'])
    else:  # ex. 13-> 14 = -1
        item.item.quantity -= int(request.POST['quantity']) - item.quantity

    item.quantity = request.POST['quantity']
    item.save()
    item.item.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", '/'))
