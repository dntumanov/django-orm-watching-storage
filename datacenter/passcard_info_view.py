from typing import List

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    """Возвращает информацию о пропуске"""
    passcard = Passcard.objects.get(passcode=passcode)
    visit_passcard_list = Visit.objects.filter(passcard=passcard)

    context = {
        "passcard": passcard,
        "this_passcard_visits": visit_passcard_list
    }
    return render(request, 'passcard_info.html', context)
