from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
import application
from .filters import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import django_filters
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout as bruh
from django.db import connection
from django.db.models import Q


def home(request):
    return render(request, 'home.html', )


def get_matches():
    return Match.objects.filter(created_date__lte=timezone.now())


def match_list_error(request):
    matches = get_matches().order_by('start_date', )
    return render(request, 'match_list_error.html',
                  {'matches': matches})


def match_list(request):
    matches = get_matches().order_by('start_date', )

    # test = Group.objects.values(name='Referee_Group').exists()
    # Group.objects.filter(user=request.user)

    return render(request, 'match_list.html',
                  {'matches': matches})


@login_required
def match_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        firststep = form.save(commit=False)
        if form.is_valid():
            try:

                # check if field is same
                results = Match.objects.filter(start_date=firststep.start_date, field=firststep.field, )
                integrity(results, firststep)

                # check if ref is same
                results = Match.objects.filter(start_date=firststep.start_date,
                                               referee=firststep.referee, )
                integrity(results, firststep)

                # check if teams are same first order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               guest_team=firststep.guest_team,
                                               )
                integrity(results, firststep)

                # check if teams are same second order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)

                # check if teams are same third order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)

                # check if teams are same third order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)


            except ValueError:
                matches = get_matches().order_by('start_date')
                return render(request, 'match_list_error.html',
                              {'matches': matches})

            match.updated_date = timezone.now()
            match.save()
            matches = get_matches().order_by('start_date')
            return render(request, 'match_list.html',
                          {'matches': matches})

    else:
        form = MatchForm(instance=match)
        return render(request, 'match_edit.html', {'form': form})


@login_required
def match_new(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        firststep = form.save(commit=False)
        if form.is_valid():
            try:
                # check if field is same
                results = Match.objects.filter(start_date=firststep.start_date, field=firststep.field, )
                integrity(results, firststep)

                # check if ref is same
                results = Match.objects.filter(start_date=firststep.start_date,
                                               referee=firststep.referee, )
                integrity(results, firststep)

                # check if teams are same first order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               guest_team=firststep.guest_team,
                                               )
                integrity(results, firststep)

                # check if teams are same second order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)

                # check if teams are same third order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)

                # check if teams are same third order
                results = Match.objects.filter(start_date=firststep.start_date,
                                               home_team=firststep.guest_team)
                integrity(results, firststep)

            except ValueError:
                matches = get_matches().order_by('start_date')
                return render(request, 'match_list_error.html',
                              {'matches': matches})
            match = form.save()
            match.updated_date = timezone.now()
            match.save()
            matches = get_matches().order_by('start_date')
            return render(request, 'match_list.html',
                          {'matches': matches})
    else:
        form = MatchForm()
    return render(request, 'match_new.html', {'form': form})

##ok try to do a check to see if the match ID's are the same between the form and the result
def integrity(results, firststep):
    errors = 0
    for obj in results:
        time = str(obj.start_time).split(":")
        print("Found start = ", time[0])
        print("Time input = ", (str(firststep.start_time).split(":")[0]))
        difference = int(str(firststep.start_time).split(":")[0]) - int(time[0])
        print("Difference = ", difference)
        print("Found ID = ", obj.id)
        print("Input ID = ", firststep.id)
        if 1 >= difference >= -1:
            errors += 1
            print("Errors: ", errors)
        if obj.id == firststep.id:
            errors -= 1
    if errors > 0:
        raise ValueError('Time constraints')


@login_required
def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    match.delete()
    return redirect('application:match_list')


@login_required
def team_list(request):
    team = Team.objects.all()
    # team = Team.objects.filter(created_date__lte=timezone.now())

    return render(request, 'team_list.html',
                  {'teams': team})


@login_required
def my_team_list(request):
    team = Team.objects.all()
    team = Team.objects.filter(coach_uid=request.user)
    # school = School.objects.filter(team__coach_uid=request.user)
    return render(request, 'my_team_list.html',
                  {'teams': team})  # , {'school': school})


@login_required
def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()

            team.updated_date = timezone.now()
            team.save()
            if request.user.is_superuser:
                teams = Team.objects.filter(created_date__lte=timezone.now())
            else:
                teams = Team.objects.filter(coach_uid=request.user)
            return render(request, 'team_list.html', {'teams': teams})
    else:
        print("else")
        form = TeamForm(instance=team)
    return render(request, 'team_edit.html', {'form': form})


@login_required
def team_new(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = TeamForm(request.POST)
            if form.is_valid():
                team = form.save()
                team.updated_date = timezone.now()
                team.save()
                teams = Team.objects.filter(created_date__lte=timezone.now())
                return render(request, 'team_list.html', {'teams': teams})
        else:
            # print("else")
            form = TeamForm()
            return render(request, 'team_new.html', {'form': form})
    else:
        return render(request, 'home.html', )


@login_required
def team_delete(request, pk):
    if request.user.is_superuser:
        team = get_object_or_404(Team, pk=pk)
        team.delete()
        return redirect('application:team_list')
    else:
        return render(request, 'home.html', )


@login_required
def player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.created_date = timezone.now()
            player.save()
            if request.user.is_superuser:
                players = Player.objects.all()
            else:
                players = Player.objects.filter(team__coach_uid=request.user)
            return render(request, 'player_list.html',
                          {'players': players})
    else:
        form = PlayerForm()
        # print("Else")
    return render(request, 'player_new.html', {'form': form})


@login_required
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('application:player_list')


@login_required
def player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.created_date = timezone.now()
            player.save()
            if request.user.is_superuser:
                players = Player.objects.all()
            else:
                players = Player.objects.filter(team__coach_uid=request.user)
            return render(request, 'player_list.html',
                          {'players': players})
    else:
        form = PlayerForm()
        # print("Else")
    return render(request, 'player_new.html', {'form': form})


@login_required
def player_list(request):
    # player = Player.objects.filter(created_date__lte=timezone.now())

    players = Player.objects.all()

    # get player team, team coach_uid and filter for coach_uid=request.
    return render(request, 'player_list.html',
                  {'players': players})


@login_required
def player_by_team_list(request):
    # player = Player.objects.filter(created_date__lte=timezone.now())
    if request.user.is_superuser:
        players = Player.objects.all()
    else:
        players = Player.objects.filter(team__coach_uid=request.user)
    # get player team, team coach_uid and filter for coach_uid=request.
    return render(request, 'player_by_team_list.html',
                  {'players': players})


@login_required
def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()

            player.updated_date = timezone.now()
            player.save()
            if request.user.is_superuser:
                players = Player.objects.all()
            else:
                players = Player.objects.filter(team__coach_uid=request.user)
            return render(request, 'player_list.html', {'players': players})
    else:
        print("else")
        form = PlayerForm(instance=player)
    return render(request, 'player_edit.html', {'form': form})


@login_required
def coach_player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = CoachPlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()

            player.updated_date = timezone.now()
            player.save()
            if request.user.is_superuser:
                players = Player.objects.all()
            else:
                players = Player.objects.filter(team__coach_uid=request.user)
            return render(request, 'player_list.html', {'players': players})
    else:
        form = CoachPlayerForm(instance=player)
    return render(request, 'coach_player_edit.html', {'form': form})


@login_required
def report_scores_list(request):
    if request.user.is_superuser:
        match = Match.objects.all()
    else:
        match = Match.objects.filter(referee_uid=request.user)
    return render(request, 'report_scores_list.html',
                  {'matches': match})


@login_required
def report_scores_by_search(request):
    match = Match.objects.filter(referee_uid=request.user)
    match_filter = MatchFilter(request.GET, queryset=match)
    match = match_filter.qs

    context = {
        'match_filter': match_filter,
        'matches': match,
        'MatchFilter': MatchFilter

    }

    return render(request, 'report_scores_by_search.html', context)


@login_required
def report_scores_by_search_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save()
            match.updated_date = timezone.now()
            match.save()
            matches = Match.objects.filter(referee_uid=request.user).order_by('start_date')
            return render(request, 'report_scores_by_search.html', {'matches': matches})
    else:
        print("else")
        form = ReportForm(instance=match)
    return render(request, 'report_scores_by_search_edit.html', {'form': form})


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def technical_manual(request):
    return render(request, 'technical_manual.html')
