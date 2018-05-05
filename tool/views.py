from django.shortcuts import render
from django.utils import timezone

from .models import Auction, Status


def auction_list(request):
    aucs = Auction.objects.filter(published_date__lte=timezone.now())
    stats = Auction.objects.filter(published_date__lte=timezone.now()).count()
    stats_win = Auction.objects.filter(win=Status.WINNER).count()

    return render(request, 'auction_list.html', {
        'aucs': aucs,
        'stats': stats,
        'stats_win': stats_win
    })
