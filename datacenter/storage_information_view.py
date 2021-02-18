from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    """Возвращает историю посещения хранилища"""
    passcard_visit_list = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visitor in passcard_visit_list:
        duration_dict = {}
        visit = Visit()
        duration = visit.get_duration(visitor.entered_at, visitor.leaved_at)
        is_strange_visit = visit.get_visit_long(duration)
        duration_dict.update(
            who_entered=visitor.passcard.owner_name,
            entered_at=visitor.entered_at,
            duration=visit.get_format_duration(duration),
            is_strange=is_strange_visit
        )
        non_closed_visits.append(duration_dict)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
