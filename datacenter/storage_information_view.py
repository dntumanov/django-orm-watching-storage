
from typing import List


from datacenter.models import Visit
from django.shortcuts import render




def storage_information_view(request):
    """Возвращает историю посещения хранилища"""
    passcard_visit_list: List[Visit] = Visit.objects.filter(leaved_at=None)
    non_closed_visits: List[dict] = []
    for visitor in passcard_visit_list:
        duration_dict = {}
        duration, is_strange_visit = Visit.get_duration()
        duration_dict.update(
            who_entered=visitor.passcard.owner_name,
            entered_at=visitor.entered_at,
            duration=duration,
            is_strange=is_strange_visit
        )
        non_closed_visits.append(duration_dict)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
