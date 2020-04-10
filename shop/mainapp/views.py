import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
import mainapp
from mainapp.models import Category, Product, Order, OrderItem, Sort


def main(request):
    categories = Category.objects.all()
    new_products = Product.objects.all().order_by('-date')[:3]
    top_products = Product.objects.all().order_by('-rating')[:6]
    sorts = Sort.objects.all()

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
               'total': total}
    return render(request, 'mainapp/index.html', content)


def search(request):
    categories = Category.objects.all()

    filters = {
        key: value
        for key, value in request.POST.items()
        if value and key in ['category', 'sort', 'length']
    }

    print(filters)

    res = Product.objects.filter(**filters)

    return render(request, 'mainapp/search.html', {'products': res, 'categories': categories})


def cart_remove(request, id):
    OrderItem.objects.get(id=id).delete()
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
    try:
        order = Order.objects.filter(user=request.session.session_key).reverse()[:1][0]  # get the last order
    except IndexError:
        order = Order.objects.create(user=request.session.session_key)

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
    item = get_object_or_404(OrderItem, id=request.POST['product'])
    item.quantity = request.POST['quantity']
    item.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", '/'))
