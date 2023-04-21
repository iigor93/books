from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-id',)

    name = models.CharField(max_length=20, verbose_name="Название")
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    author = models.CharField(max_length=30, verbose_name="Автор")
    description = models.CharField(max_length=512, verbose_name="Описание", null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name="Цена")
