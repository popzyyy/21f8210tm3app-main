from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from django.urls import path, re_path
from django.contrib import admin
from django.urls import path, include
from .views import SignUpView

app_name = 'application'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    re_path(r'^home/$', views.home, name='home'),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('match_list/', views.match_list, name='match_list'),
    path('match_list_error/', views.match_list_error, name='match_list_error'),
    path('match/<int:pk>/edit/', views.match_edit, name='match_edit'),
    path('match/create/', views.match_new, name='match_new'),
    path('match/<int:pk>/delete/', views.match_delete, name='match_delete'),
    path('team/create/', views.team_new, name='team_new'),
    path('team_list', views.team_list, name='team_list'),
    path('my_team_list', views.my_team_list, name='my_team_list'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('player_list', views.player_list, name='player_list'),
    path('player/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('coach/player/<int:pk>/edit/', views.coach_player_edit, name='coach_player_edit'),
    path('player/<int:pk>/delete/', views.player_delete, name='player_delete'),
    path('player/create/', views.player_new, name='player_new'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('report_scores/', views.report_scores_list, name='report_scores_list'),
    path('report_scores/search', views.report_scores_by_search, name='report_scores_by_search'),
    path('report_scores/search/<int:pk>/', views.report_scores_by_search_edit, name='report_scores_by_search_edit'),
    #path('stats/', views.stats, name='stats'),
    path('technical_manual/', views.technical_manual, name='technical_manual'),
    path('player_by_team_list/', views.player_by_team_list, name='player_by_team_list'),

]
