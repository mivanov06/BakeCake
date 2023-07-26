from django.db import models

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
