import django_filters
from .models import *


class MatchFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = 'id', 'home_team', 'guest_team', 'field_id',


class PlayerFilter(django_filters.FilterSet):
    class Meta:
        model = Player
        fields = 'id', 'team', 'first_name', 'last_name',


class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = 'id', 'school', 'name', 'coach_uid',
