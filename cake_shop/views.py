import json
from django.shortcuts import render, redirect
from django.http import JsonResponse

from cake_shop.models import Layer, Shape, Topping, Berry, Decor, Client, Order

from cake_shop.models import Cake


def index(request):
    data = {
        'js_data': {
            'Levels': ['не выбрано'],
            'Forms': ['не выбрано'],
            'Toppings': ['не выбрано'],
            'Berries': ['не выбрано'],
            'Decors': ['не выбрано'],
        },
        'layers': [],
        'shapes': [],
        'toppings': [],
        'berries': [],
        'decors': [],
        'js_costs': {
            'Levels': [0],
            'Forms': [0],
            'Toppings': [0],
            'Berries': [0],
            'Decors': [0],
            'Words': 500,
        }
    }
    for layer in Layer.objects.all():
        data['js_data']['Levels'].append(layer.title)
        data['js_costs']['Levels'].append(int(layer.price))
        data['layers'].append(layer.title)

    for shape in Shape.objects.all():
        data['js_data']['Forms'].append(shape.title)
        data['js_costs']['Forms'].append(int(shape.price))
        data['shapes'].append(shape.title)

    for topping in Topping.objects.all():
        data['js_data']['Toppings'].append(topping.title)
        data['js_costs']['Toppings'].append(int(topping.price))
        data['toppings'].append(topping.title)

    for berry in Berry.objects.all():
        data['js_data']['Berries'].append(berry.title)
        data['js_costs']['Berries'].append(int(berry.price))
        data['berries'].append(berry.title)

    for decor in Decor.objects.all():
        data['js_data']['Decors'].append(decor.title)
        data['js_costs']['Decors'].append(int(decor.price))
        data['decors'].append(decor.title)

    return render(request, 'index.html', context=data)


def order(request):
    print(request)
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)

    return redirect('index')


def lk(request):
    client = Client.objects.filter(phone='88005553535').first()
    mail = client.mail
    if not mail:
        mail = 'my@mail.ru'

    orders = Order.objects.filter(client=client)
    serialize_orders = []
    for order in orders:
        order = {
            'id': order.id,
            'cakes': order.cakes.all(),
            'price': order.order_price,
            'delivery_time': order.delivery_time
        }
        serialize_orders.append(order)

    data = {
        'js_client': {
                "name": client.name,
                "phone": client.phone,
                "mail": mail,
                "address": client.address
        },
        'orders': orders
    }

    return render(request, 'lk_template.html', context=data)


def lk_order(request):
    return render(request, 'lk-order.html')


def serialize_cakes(cakes):
    serialized = []
    for cake in cakes:
        serialized.append(
            {
                'title': cake.title,
                'description': cake.description,
                'picture': cake.picture.url,
                'category': cake.category,
                'layers': cake.layers,
                'shape': cake.shape,
                'toppings': cake.toppings,
                'berries': cake.berries,
                'decor': cake.decor,
                'price':cake.get_price()
            }
        )
    return serialized


def cakes(request):
    default_cakes = Cake.objects.filter(default=True)
    context = {
        'cakes': serialize_cakes(default_cakes)
    }
    return render(request, 'cakes.html', context)
