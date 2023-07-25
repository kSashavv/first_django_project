from django import forms
from .models import Application, Post


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['status']
        labels = {
            'first_name': 'Имя',
            'second_name': 'Фамилия',
            'email': 'Электронная почта',
            'phone_number': 'Номер телефона',
            'description': 'Описание',
            'patent_name': 'Название патента',
            'attached_file': 'Прикрепить файл',
            'application_type': 'Тип заявки',
            'status': 'Статус',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_posted']
        labels = {
            'title': 'Название',
            'content': 'Текст статьи',
            'date_posted': 'Время публикации',
            'author': 'Автор'
        }
