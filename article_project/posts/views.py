from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Category, Tag, Contact
from .form import ContactForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    articles = Post.objects.filter(status="published").order_by('-date_published')
    categories = Category.objects.all()

    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)).distinct()

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)
    context = {'articles': articles_paginator, "categories": categories}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def categories(request, category_slug):
    articles = Post.objects.filter(status="published")
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)).distinct()

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        articles = articles.filter(category = category)

    context = {'articles': articles, "categories": categories}
    template = loader.get_template('category.html')
    return HttpResponse(template.render(context, request))


def tags(request, tag_slug):
    articles = Post.objects.filter(status="published").order_by('-date_published')
    categories = Category.objects.all
    tag = Tag.objects.all()
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)).distinct()

    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        articles= articles.filter(tag = tag)

    context = {'articles': articles, 'categories': categories}
    template = loader.get_template('tags.html')
    return HttpResponse(template.render(context, request))


def PostDetails(request, post_slug):
    article = get_object_or_404(Post, slug=post_slug)
    categories = Category.objects.all

    template = loader.get_template('post_details.html')

    context = {
        'article': article, 'categories': categories
    }

    return HttpResponse(template.render(context, request))


def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save()
            return redirect("contactsuccess")
    else:
        form = ContactForm()

    categories = Category.objects.all

    context = {
        'form' : form, "categories": categories
    }
    return render(request, 'contact.html', context)


def Contactsuccess(request):
    return render(request, 'contactsuccess.html')




