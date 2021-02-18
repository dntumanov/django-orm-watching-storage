from typing import List

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    """Возвращает информацию о пропуске"""
    passcard: List[Passcard] = Passcard.objects.get(passcode=passcode)
    visit_passcard_list: List[Visit] = Visit.objects.filter(passcard=passcard)

    this_passcard_visits: List[dict] = []

    for passcard_visit in visit_passcard_list:
        passcard_visit_dict = {}
        visit = Visit()
        duration = visit.get_duration(passcard_visit.entered_at, passcard_visit.leaved_at)
        is_strange_visit = visit.get_visit_long(duration)
        passcard_visit_dict.update(
            entered_at=passcard_visit.entered_at,
            duration=visit.get_format_duration(duration),
            is_strange=is_strange_visit
        )
        this_passcard_visits.append(passcard_visit_dict)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
