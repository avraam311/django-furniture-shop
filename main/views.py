from django.shortcuts import render
from django.http import HttpResponse

from typing import Any


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Очень крутой магаз'
    }

    return render(request, 'main/about.html', context)
