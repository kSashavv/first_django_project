from django.shortcuts import render
from .forms import PostForm
from .models import Post, Category


title = ['Главная страница', 'Добавте статью', 'Сатьи по категории', 'Статья', 'Все категории']


def blog(request):
    article = Post.objects.all().select_related('cat')
    return render(request, 'blog.html', {'article': article,  'title': title[0]})


def create_article(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create_article.html', {'form': form, 'title': title[1]})


def show_post(request, post_id):
    article = Post.objects.get(id=post_id)
    return render(request, 'article.html', {'article': article, 'title': title[3]})


def show_cat(request, cat_id):
    w = Post.objects.filter(cat=cat_id)
    return render(request, 'show_category.html', {'w': w, 'title': title[2]})


def all_categories(request):
    cat = Category.objects.all()
    return render(request, 'category.html', {'cat': cat, 'title': title[4]})
