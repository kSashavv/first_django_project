from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Application(models.Model):
    APPLICATION_TYPES = (
        ('invention', 'Патент на изобретение'),
        ('trademark', 'Регистрация товарного знака'),
        # Добавьте другие типы заявок, если необходимо
    )
    status_choices = (
        ('processing', 'В обработке'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    )

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    patent_name = models.CharField(max_length=255)
    attached_file = models.FileField(upload_to='media/')
    application_type = models.CharField(max_length=20, choices=APPLICATION_TYPES)
    status = models.CharField(max_length=20, choices=status_choices)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.application_type}'

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_posted', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
