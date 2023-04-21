from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователей'

    column_name = models.BooleanField(verbose_name="Колонка Название", default=True)
    column_title = models.BooleanField(verbose_name="Колонка Заголовок", default=True)
    column_author = models.BooleanField(verbose_name="Колонка Автор", default=True)
    column_description = models.BooleanField(verbose_name="Колонка Описание", default=True)
    column_price = models.BooleanField(verbose_name="Колонка Цена", default=True)
