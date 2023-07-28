from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader, select_autoescape

from cake_shop.models import Cake, Client, Order
from cake_shop.models import Berry, Decor, Layer, Shape, Topping


def index(request):
    return render(request, 'index.html')


def lk(request):
    return render(request, 'lk.html')


def lk_order(request):
    return render(request, 'lk-order.html')


def index_template(request):
    berries = Berry.objects.all()
    decors = Decor.objects.all()
    layers = Layer.objects.all()
    shapes = Shape.objects.all()
    toppings = Topping.objects.all()
    render_customize(berries, decors, layers, shapes, toppings)
    context = {
        'berries': berries,
        'decors': decors,
        'layers': layers,
        'shapes': shapes,
        'toppings': toppings,
    }
    return render(request, 'index_template.html', context)
    #  TODO Сделать форму для оплаты (моя корзина ?)
    #  TODO В форме при подтверждении оплаты сохранить заказ в базе
    #  TODO добавить ссылки
    #  TODO Сделать взаимодействие index.js и базы


def lk_template(request):
    client_id = 1  # TODO получать id при входе по номеру телефона
    #  TODO Сделать номер телефона уникальным полем
    client = Client.objects.get(id=client_id)  # TODO добавить взаимодействие с lk.js
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


def render_customize(berries, decors, layers, shapes, toppings):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('templates/customize_template.html')

    rendered_page = template.render(
        berries=berries,
        decors=decors,
        layers=layers,
        shapes=shapes,
        toppings=toppings
    )

    with open(f'templates/shop-base/rendered_customize.html', 'w', encoding="utf-8") as file:
        file.write('{% verbatim %}')
        file.write('\n')
        file.write(rendered_page)
        file.write('\n')
        file.write('{% endverbatim %}')