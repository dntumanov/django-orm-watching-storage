from django.db import models
from datetime import timedelta
from django.utils import timezone


class Passcard(models.Model):
    """Описание модели пропуска"""
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    """Описание модели визитов в хранилище"""

    TIME_IN_SECOND: int = 3600

    # Описание модели
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    @staticmethod
    def get_local_time(current_time):
        """Возвращает текущее местное время"""
        return timezone.localtime(current_time)

    @staticmethod
    def get_format_duration(duration_time):
        """Возвращает время в формате HH:MM"""
        return str(duration_time)[0:7]

    @staticmethod
    def check_is_visit_long(duration):
        """Проверяет визит в хранилище на подозрительность"""
        if duration.total_seconds() > Visit.TIME_IN_SECOND:
            return True
        else:
            return False

    @classmethod
    def get_duration(cls):
        """Возвращает продолжительность нахождения в хранилище"""
        entered_at_time = cls.get_local_time(cls.entered_at)
        time_now = cls.get_local_time(timezone.now())
        duration = time_now - entered_at_time
        if cls.leaved_at:
            leaved_at_time = cls.get_local_time(cls.leaved_at)
            duration = leaved_at_time - entered_at_time
        return cls.get_format_duration(duration), cls.check_is_visit_long(duration)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
