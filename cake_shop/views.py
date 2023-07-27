from django.shortcuts import render, redirect
from cake_shop.models import Layer, Shape, Topping, Berry, Decor


def index(request):
    data = {
        'js_data': {
            'Levels': ['не выбрано'],
            'Forms': ['не выбрано'],
            'Toppings': ['не выбрано'],
            'Berries': ['не выбрано'],
            'Decors': ['не выбрано'],
        }
    }
    for layer in Layer.objects.all():
        data['js_data']['Levels'].append(layer.title)

    for shape in Shape.objects.all():
        data['js_data']['Forms'].append(shape.title)

    for topping in Topping.objects.all():
        data['js_data']['Toppings'].append(topping.title)

    for berry in Berry.objects.all():
        data['js_data']['Berries'].append(berry.title)

    for decor in Decor.objects.all():
        data['js_data']['Decors'].append(decor.title)

    return render(request, 'index.html', context=data)


def order(request):
    if request.GET:
        print(request.GET)
    return redirect('../')


def lk(request):
    return render(request, 'lk.html')


def lk_order(request):
    return render(request, 'lk-order.html')
