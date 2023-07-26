from django.contrib import admin
from cake_shop.models import Cake
from cake_shop.models import Order
from cake_shop.models import OrderedCake
from cake_shop.models import Client
from cake_shop.models import Layer
from cake_shop.models import Shape
from cake_shop.models import Topping
from cake_shop.models import Berry
from cake_shop.models import Decor


class OrderedCakeInline(admin.TabularInline):
    model = OrderedCake
    extra = 0


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'category',
        'default',
    ]
    list_display = [
        'title',
        'category',
        'default',
    ]


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]
    list_display = [
        'title',
        'price',
    ]


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]
    list_display = [
        'title',
        'price',
    ]


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]
    list_display = [
        'title',
        'price',
    ]


@admin.register(Berry)
class BerryAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]
    list_display = [
        'title',
        'price',
    ]


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]
    list_display = [
        'title',
        'price',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = [
        'create_time',
        'client',
        'order_status',
    ]
    list_display = [
        'create_time',
        'client',
        'order_status',
    ]
    inlines = [
        OrderedCakeInline,
    ]
"""
from cake_shop.models import Form, Berry, Decore, Topping, Level, Cake

# Register your models here.


@admin.register(Form)
class AdminForm(admin.ModelAdmin):
    fields = ('price', 'title')
    list_display = ('title',)


@admin.register(Berry)
class AdminBerry(admin.ModelAdmin):
    fields = ('price', 'status', 'title')
    list_display = ('title', 'status')


@admin.register(Decore)
class AdminDecore(admin.ModelAdmin):
    fields = ('price', 'status', 'title')
    list_display = ('title', 'status')


@admin.register(Topping)
class AdminTopping(admin.ModelAdmin):
    fields = ('price', 'status', 'title')
    list_display = ('title', 'status')


@admin.register(Level)
class AdminLevel(admin.ModelAdmin):
    fields = ('price', 'title')
    list_display = ('title',)


@admin.register(Cake)
class AdminCake(admin.ModelAdmin):
    fields = ('levels', 'form', 'berries', 'topping', 'decore', 'text', 'comment')
    list_display = ('id',)
"""
