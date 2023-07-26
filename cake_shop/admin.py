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


class LayerInline(admin.TabularInline):
    model = Layer
    extra = 0


class ShapeInline(admin.TabularInline):
    model = Shape
    extra = 0


class ToppingInline(admin.TabularInline):
    model = Topping
    extra = 0


class BerryInline(admin.TabularInline):
    model = Berry
    extra = 0


class DecorInline(admin.TabularInline):
    model = Decor
    extra = 0


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
