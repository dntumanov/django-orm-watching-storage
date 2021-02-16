from datetime import timedelta, datetime

from typing import Tuple

from django.utils import timezone

# TIME_IN_SECOND: int = 3600
#
# TEXT_YES: str = 'да'
# TEXT_NO: str = 'нет'


def get_local_time(current_time):
    """Возвращает текущее местное время"""
    return timezone.localtime(current_time)


def get_format_duration(duration_time: timedelta) -> str:
    """Возвращает время в формате HH:MM"""
    return str(duration_time)[0:7]

