from django.db import models


class OrderedCake(models.Model):
    order = models.ForeignKey(
        'Order',
        related_name='ordered_cakes',
        verbose_name='заказы',
        null=True,
        on_delete=models.SET_NULL,
    )
    cake = models.ForeignKey(
        'Cake',
        related_name='ordered_cakes',
        verbose_name='торты',
        null=True,
        on_delete=models.SET_NULL,
    )
    quantity = models.IntegerField(verbose_name='Количество тортов', default=1)
    comment = models.TextField(
        'комментарий к торту',
        blank=True,
    )
    cake_text = models.TextField(
        'текст на торте',
        blank=True,
    )


class Order(models.Model):
    TIME_PERIODS = (
        ('01', '08:00-10:00'),
        ('02', '10:00-12:00'),
        ('03', '12:00-14:00'),
        ('04', '14:00-16:00'),
        ('05', '16:00-18:00'),
        ('06', '18:00-20:00'),
        ('07', '20:00-22:00'),
    )
    DELIVERY_TYPES = (
        ('01', 'Курьером'),
        ('02', 'Самовывоз'),
    )
    STATUSES = (
        ('01', 'Оформлен'),
        ('02', 'В доставке'),
        ('03', 'Доставлен'),
    )
    client = models.ForeignKey(
        'Client',
        verbose_name='клиент',
        related_name='orders',
        null=True,
        on_delete=models.SET_NULL,
    )
    cakes = models.ManyToManyField(
        'Cake',
        through='OrderedCake',
        verbose_name='торты',
        related_name='orders',
    )
    comment = models.TextField(
        'комментарий к заказу',
        blank=True,
    )
    order_price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=19,
        verbose_name='Сумма заказа',
        decimal_places=2
    )
    create_time = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True
    )
    delivery_date = models.DateField(
        verbose_name='время создания',
        blank=True,
        null=True,
    )
    delivery_time = models.CharField(
        max_length=2,
        choices=TIME_PERIODS,
        blank=True,
    )
    delivery_type = models.CharField(
        max_length=2,
        choices=DELIVERY_TYPES,
        blank=True,
    )
    order_status = models.CharField(
        max_length=2,
        choices=STATUSES,
        default='01',
    )
    urgency = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.delivery_time)}'

    # TODO Добавить расчет цены


class Client(models.Model):
    name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Телефон', max_length=12)
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4'
     )

    def __str__(self):
        return self.name


class Cake(models.Model):
    CATEGORY = (
        ('01', 'На день рождения'),
        ('02', 'На свадьбу'),
        ('03', 'На чаепитие'),
    )
    title = models.CharField('название торта', max_length=200, blank=True)
    description = models.TextField(
        'описание торта',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='изображение торта',
        blank=True,
        null=True,
    )
    default = models.BooleanField('торт в ассортименте', default=False)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        blank=True,
    )
    layers = models.ForeignKey(
        'Layer',
        verbose_name='слои',
        related_name='cakes',
        null=True,
        on_delete=models.SET_NULL,
    )
    shape = models.ForeignKey(
        'Shape',
        verbose_name='форма',
        related_name='cakes',
        null=True,
        on_delete=models.SET_NULL,
    )
    toppings = models.ForeignKey(
        'Topping',
        verbose_name='топинги',
        related_name='cakes',
        null=True,
        on_delete=models.SET_NULL,
    )
    berries = models.ForeignKey(
        'Berry',
        verbose_name='ягоды',
        related_name='cakes',
        null=True,
        on_delete=models.SET_NULL,
    )
    decor = models.ForeignKey(
        'Decor',
        verbose_name='декор',
        related_name='cakes',
        null=True,
        on_delete=models.SET_NULL,
    )

    price = models.FloatField(blank=True, null=True, verbose_name='Цена')

    def __str__(self):
        return self.title

    def get_price(self):
        # total скорее всего 0.00 писать надо
        total = 0
        total += self.layers.price
        total += self.shape.price
        for berry in Berry.objects.filter(cakes__id=self.id):
            total += berry.price
        for topping in Topping.objects.filter(cakes__id=self.id):
            total += topping.price
        return total

    def save(self):
        # if self.text:
        #     price = 500
        # else:
        #     price = 0
        price = 0
        price += self.layers.price
        price += self.shape.price
        price += self.toppings.price
        price += self.berries.price
        price += self.decor.price
        self.price = price
        super().save()


class Layer(models.Model):
    title = models.CharField(
        verbose_name='Количество слоев',
        max_length=32,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=19,
        verbose_name='Цена',
        decimal_places=2,
    )

    def __str__(self):
        return f'{str(self.title)}'


class Shape(models.Model):
    title = models.CharField(verbose_name='Форма коржа', max_length=32)
    price = models.DecimalField(
        max_digits=19,
        verbose_name='Цена',
        decimal_places=2,
    )

    def __str__(self):
        return f'{str(self.title)}'

"""
# Create your models here.


class Berry(models.Model):
    title = models.CharField(
        null=True,
        max_length=20,
        verbose_name='Ягода'
    )
    price = models.FloatField(
        null=True,
        verbose_name='Цена'
    )
    status = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    class Meta:
        verbose_name = 'Ягоды'
        verbose_name_plural = 'Ягоды'

    def __str__(self):
        return self.title


class Decore(models.Model):
    title = models.CharField(
        null=True,
        max_length=20,
        verbose_name='Декор'
    )
    price = models.FloatField(
        null=True,
        verbose_name='Цена'
    )
    status = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декор'

    def __str__(self):
        return self.title


class Topping(models.Model):
    title = models.CharField(
        null=True,
        max_length=20,
        verbose_name='Топинг'
    )
    price = models.FloatField(
        null=True,
        verbose_name='Цена'
    )
    status = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    class Meta:
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинг'

    def __str__(self):
        return self.title


class Form(models.Model):
    title = models.CharField(
        null=True,
        max_length=20,
        verbose_name='Форма'
    )
    price = models.FloatField(
        null=True,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Формы'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return self.title
"""


class Topping(models.Model):
    title = models.CharField(verbose_name='Топпинг', max_length=32)
    price = models.DecimalField(
        max_digits=19,
        verbose_name='Цена',
        decimal_places=2,
    )

    def __str__(self):
        return self.title


class Berry(models.Model):
    title = models.CharField(verbose_name='Ягода', max_length=32)
    price = models.DecimalField(
        max_digits=19,
        verbose_name='Цена',
        decimal_places=2,
    )

    def __str__(self):
        return self.title


class Decor(models.Model):
    title = models.CharField(verbose_name='Декор', max_length=32)
    price = models.DecimalField(
        max_digits=19,
        verbose_name='Цена',
        decimal_places=2,
    )

    def __str__(self):
        return self.title
    
"""
class Level(models.Model):
    title = models.IntegerField(
        null=True,
        verbose_name='Уровни'
    )
    price = models.FloatField(
        null=True,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Уровни'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return str(self.title)


class Cake(models.Model):
    levels = models.ForeignKey(
        Level,
        on_delete=models.DO_NOTHING,
        verbose_name='Уровни'
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.DO_NOTHING,
        verbose_name='Форма'
    )
    topping = models.ForeignKey(
        Topping,
        on_delete=models.DO_NOTHING,
        verbose_name='Топинг'
    )
    berries = models.ForeignKey(
        Berry,
        on_delete=models.DO_NOTHING,
        verbose_name='Ягода'
    )
    decore = models.ForeignKey(
        Decore,
        on_delete=models.DO_NOTHING,
        verbose_name='Декор'
    )
    text = models.CharField(
        blank=True,
        max_length=50,
        verbose_name='Надпись'
    )
    comment = models.TextField(
        null=True,
        blank=True,
        verbose_name='Комментарий к торту'
    )

    class Meta:
        verbose_name = 'Торты'
        verbose_name_plural = 'Торты'

    def __str__(self):
        return str(self.id)
"""
