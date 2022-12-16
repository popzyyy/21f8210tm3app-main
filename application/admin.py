from django.contrib import admin
from .models import School, Team, Player, Field, Referee, Match


class FieldList(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner_org', 'phone')
    list_filter = ('id', 'name', 'owner_org')
    search_fields = ('id', 'name')
    ordering = ['id']


class RefereeList(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'phone', 'email')
    list_filter = ('last_name', 'email')
    search_fields = ('Last_name', 'email')
    ordering = ['last_name']


class MatchList(admin.ModelAdmin):
    list_display = ('id', 'home_team', 'field',)
    list_filter = ('id', 'home_team',)
    search_fields = ('id', 'home_team')
    ordering = ['id']


class SchoolList(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'phone')
    list_filter = ('id', 'name', 'contact')
    search_fields = ('id', 'name')
    ordering = ['id']


class TeamList(admin.ModelAdmin):
    list_display = ('name', 'school', 'coach', 'coach_phone')
    list_filter = ('school', 'name')
    search_fields = ('school', 'name')
    ordering = ['school']


class PlayerList(admin.ModelAdmin):
    list_display = ('team', 'first_name', 'last_name', 'position')
    list_filter = ('team', 'last_name', 'position')
    search_fields = ('team', 'last_name', 'position')
    ordering = ['team']

# Register your models here.


admin.site.register(School, SchoolList)
admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
admin.site.register(Field, FieldList)
admin.site.register(Referee, RefereeList)
admin.site.register(Match, MatchList)
