from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Recept, Kuchar, Kategorie


def index(request):
    kategorie = 'dezerty'
    context = {
        'nadpis': kategorie,
        'recepty': Recept.objects.order_by('nazev').filter(kategorie__nazev=kategorie),
        'kategorie': Kategorie.objects.all()
    }
    return render(request, 'index.html', context=context)


def seznam_receptu(request):
    context = {
        'nadpis': 'Seznam receptů',
        'data': Recept.objects.all(),
    }
    return render(request, 'recepty/seznam.html', context=context)


def detail_receptu(request, pk=1):
    context = {
        'titulek': 'Detail receptu',
        'recept': Recept.objects.get(id=pk),
    }
    return render(request, 'recepty/detail.html', context=context)


def orm_tester(request):
    dotaz = Recept.objects.filter(cas_pripravy__lte=30).order_by('cas_pripravy', 'id')
    try:
        data = dotaz.values()
        print(list(data))
    except Recept.DoesNotExist:
        raise Http404("Žádné recepty nebyly nalezeny.")
    context = {
        'data': list(data),
        'sloupce': list(data.first().keys()) if data else [],
    }
    return render(request, 'orm.html', context=context)


def seznam_kucharu(request):
    seznam = Kuchar.objects.order_by('prijmeni')
    context = {
        'seznam_kucharu': seznam,
    }
    return render(request, 'recepty/kuchari.html', context)


def detail_kuchare(request, pk):
    kuchar = get_object_or_404(Kuchar.objects.annotate(pocet_receptu=Count('recept')), pk=pk)
    recepty = kuchar.recepty.all()
    context = {
        'titulek': 'Detail kuchaře',
        'kuchar': kuchar,
        'recepty': recepty,
    }
    return render(request, 'recepty/detail-kuchare.html', context)
