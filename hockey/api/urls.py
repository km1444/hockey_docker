from django.urls import path

from .views import (
    PlayerDetail, PlayerList, PlayerListTeamSeason, PlayerMostGoalsList,
    SeasonLeadersTeam, TeamHistory, TeamList,
)

urlpatterns = [
    path('players/', PlayerList.as_view()),
    path('players_most_goals/', PlayerMostGoalsList.as_view()),
    path('players/<int:id>/', PlayerDetail.as_view()),
    path('teams/', TeamList.as_view()),
    path('teams/history/<str:team>/', TeamHistory.as_view()),
    path('teams/season_leaders/<str:team>/', SeasonLeadersTeam.as_view()),
    path(
        'team/<str:team>/<str:season>/', PlayerListTeamSeason.as_view()
    ),
]
