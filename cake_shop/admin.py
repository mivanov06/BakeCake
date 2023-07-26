from django.contrib import admin

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
    fields = ('levels', 'form', 'berries', 'topping', 'decore', 'text', 'comment', 'price')
    list_display = ('id',)
    readonly_fields = ('price',)