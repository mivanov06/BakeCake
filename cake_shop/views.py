from django.shortcuts import render

from cake_shop.models import Cake, Client, Order


def index(request):
    return render(request, 'index.html')


def lk(request):
    return render(request, 'lk.html')


def lk_order(request):
    return render(request, 'lk-order.html')


def lk_template(request):
    client_id = 1  # TODO получать id при входе по телефону
    client = Client.objects.get(id=client_id)  # TODO добавить взаимодействие с js
    orders = Order.objects.filter(client=client)

    context = {
        'orders': orders,
        'client': client,
    }
    return render(request, 'lk_template.html', context)


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
                'decor': cake.decor
            }
        )
    return serialized


def cakes(request):
    default_cakes = Cake.objects.filter(default=True)
    context = {
        'cakes': serialize_cakes(default_cakes)
    }
    return render(request, 'cakes.html', context)
