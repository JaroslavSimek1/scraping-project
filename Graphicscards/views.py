from django.http import HttpResponse
from .models import GraphicsCards
from Graphicscards.czc import find_all_products_czc
from Graphicscards.mironet import find_all_products_mironet
from django.shortcuts import render, redirect
from .models import GraphicsCards


def find_graphics_cards(request):
    GraphicsCards.objects.all().delete()
    find_all_products_czc()
    find_all_products_mironet()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def from_cheap(request):
    g_card = GraphicsCards.objects.all()
    g_card = sorted(g_card, key = lambda x : x.price)
    g_chip = request.POST.get('g_chip')
    submit_button = request.POST.get('Submit')
    context = {'g_chip': g_chip, 'submitbutton': submit_button, 'graphiccards': g_card}

    return render(request, 'graphics_cards.html', context)



def from_expensive(request):
    g_card = GraphicsCards.objects.all()
    g_card = sorted(g_card, key = lambda x : x.price, reverse=True)
    g_chip = request.POST.get('g_chip')
    submit_button = request.POST.get('Submit')
    context = {'g_chip': g_chip, 'submitbutton': submit_button, 'graphiccards': g_card}

    return render(request, 'graphics_cards.html', context)

def start(request):
    return render(request, 'index.html',)


def about(request):
    return render(request, 'about.html',)























