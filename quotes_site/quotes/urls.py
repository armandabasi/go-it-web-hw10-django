from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.home, name="home"),
    path("quotes/", views.show_quotes, name="quotes"),
    path('quotes/<int:page>', views.show_quotes, name="quotes_paginate"),
    path("quotes/add_author/", views.add_author, name="add_author"),
    path("quotes/add_quote/", views.add_quote, name="add_quote"),
    path("quotes/show_author/", views.show_author, name="show_author"),
]
