from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import AuthorForm, QuoteForm
from .utils import get_mongodb
from django.core.paginator import Paginator


def home(request):
    return render(request, "quotes/index.html", context={"title": "QuoteHive"})


def show_quotes(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/quotes.html", context={"title": "QuoteHive", "quotes": quotes_on_page})


def show_author(request):
    return render(request, "quotes/show_author.html", context={"title": "QuoteHive"})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:quotes")
        else:
            return render(request, "quotes/add_author.html",
                          context={"form": AuthorForm(), "title": "QuoteHive: new author"})
    return render(request, "quotes/add_author.html", context={"form": AuthorForm(), "title": "QuoteHive: new author"})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to="quotes:quotes")
        else:
            return render(request, "quotes/add_quote.html",
                          context={"form": QuoteForm(), "title": "QuoteHive: new quote"})
    return render(request, "quotes/add_quote.html", context={"form": QuoteForm(), "title": "QuoteHive: new quote"})
