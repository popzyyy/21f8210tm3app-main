from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class MatchForm(forms.ModelForm):
    start_time = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'time'}
        )
    )
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    class Meta:
        model = Match
        fields = (
            'home_team',
            'guest_team',
            'field',
            'referee',
            'referee_uid',
            'start_time',
            'start_date',
            'home_team_score',
            'guest_team_score',
            'match_notes',
            'match_players_goals_scored',)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = (
            'id',
            'home_team_score',
            'guest_team_score',
            'match_notes',
            'match_players_goals_scored',)


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'id',
            'school',
            'name',
            'coach_uid',
            'coach',
            'coach_email',
            'coach_phone',)


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'team',
            'first_name',
            'last_name',
            'position')

class CoachPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'first_name',
            'last_name',
            'position')

class ModelForm(forms.ModelForm):
    start_time = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'time'}
        )
    )
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Match
        fields = (
            'home_team',
            'guest_team',
            'field',
            'referee',
            'referee_uid',
            'start_time',
            'start_date',
            'home_team_score',
            'guest_team_score',
            'match_notes',
            'match_players_goals_scored',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(min_length=3, max_length=30, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
