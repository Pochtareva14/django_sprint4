from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404
from blog.models import Post, Category

# Create your views here.


def index(request):
    template = 'blog/index.html'
    now = timezone.now()
    post_list = Post.objects.filter(
        pub_date__lte=now,  # Дата публикации не позже текущего времени
        is_published=True,         # Публикация должна быть опубликована
        category__is_published=True  # Категория должна быть опубликована
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context=context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    # Проверяем условия для генерации ошибки 404
    if post.pub_date > timezone.now():
        raise Http404("Публикация еще не опубликована.")
    if not post.is_published:
        raise Http404("Публикация не найдена или не опубликована.")
    if post.category and not post.category.is_published:
        raise Http404("Категория публикации не найдена или не опубликована.")
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    # Получаем категорию по slug
    category = get_object_or_404(Category, slug=category_slug)

    # Проверяем, опубликована ли категория
    if not category.is_published:
        raise Http404("Категория не найдена или не опубликована.")

    # Получаем текущую дату и время
    now = timezone.now()

    # Фильтруем посты по категории, опубликованным статусом и дате публикации
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now
    )
    context = {'category_slug': category_slug,
               'posts': posts}
    return render(request, template, context)
