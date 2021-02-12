from datetime import timedelta, datetime

from typing import Tuple

from django.utils import timezone

TIME_IN_SECOND: int = 3600

TEXT_YES: str = 'да'
TEXT_NO: str = 'нет'


def get_local_time(current_time):
    """Возвращает текущее местное время"""
    return timezone.localtime(current_time)


def get_format_duration(duration_time: timedelta) -> str:
    """Возвращает время в формате HH:MM"""
    return str(duration_time)[0:7]


def check_is_visit_long(duration: timedelta) -> str:
    """Проверяет визит на подозрительность"""
    if duration.total_seconds() > TIME_IN_SECOND:
        return TEXT_YES
    else:
        return TEXT_NO


def get_duration(entered_at_time: datetime, leaved_at_time: datetime) -> Tuple[str, str]:
    """Возвращает продолжительность нахождения в хранилище"""
    entered_at_time = get_local_time(entered_at_time)
    time_now = get_local_time(timezone.now())
    duration = time_now - entered_at_time
    if leaved_at_time:
        leaved_at_time = get_local_time(leaved_at_time)
        duration = leaved_at_time - entered_at_time
    return get_format_duration(duration), check_is_visit_long(duration)
