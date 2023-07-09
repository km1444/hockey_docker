from django.contrib.postgres.aggregates.general import StringAgg
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import (
    Player, Playoff, Statistic, TeamForTable, TeamForTable2Round,
)
from .secondary import (
    prev_next_season, top_goal, top_point, top_season_goal, top_season_point,
)


def index(request):
    # контекст главной страницы
    total_points_for_players = Statistic.objects.values(
        'name__id', 'name__name').annotate(
            game=Sum('game'), point=Sum('point')).order_by(
                '-point', 'game').filter(point__gte=200)
    template = 'posts/index.html'
    context = {
        'page_obj': total_points_for_players,
        'table_name': 'Career Leaders for Points'
    }
    return render(request, template, context)


def team_players_in_season(request, team, season):
    # статистика игроков одной команды за сезон
    team_statistic = Statistic.objects.filter(
        team__title=team, season__name=season
    )
    template = 'posts/team_players_in_season.html'
    context = {
        'team': team,
        'season': season,
        'previous_season': prev_next_season(season)[1],
        'next_season': prev_next_season(season)[0],
        'page_obj': team_statistic,
    }
    return render(request, template, context)


def player_detail(request, id):
    """статистика игрока за карьеру, перечень всех сезонов
    в высшей лиге"""
    player = get_object_or_404(Player, id=id)
    player_seasons = player.statistics.order_by('season__name')
    count = player_seasons.values('season').distinct().count()
    game = sum(i.game for i in player_seasons)
    goal = sum(i.goal for i in player_seasons)
    assist = sum(i.assist for i in player_seasons)
    point = sum(i.point for i in player_seasons)
    penalty = sum(i.penalty for i in player_seasons)
    amount_teams = player_seasons.values('team__title').distinct().count()
    group_teams = player_seasons.values('team__title').annotate(
        game=Sum('game'),
        goal=Sum('goal'),
        assist=Sum('assist'),
        point=Sum('point'),
        penalty=Sum('penalty')
    ).order_by('-game')
    position = player_seasons[0].position
    template = 'posts/profile.html'
    context = {
        'player': player,
        'count': count,
        'page_obj': player_seasons,
        'game': game,
        'goal': goal,
        'assist': assist,
        'point': point,
        'penalty': penalty,
        'position': position,
        'group_teams': group_teams,
        'amount_teams': amount_teams,
    }
    return render(request, template, context)


def best_of_season(request, season, stat_rule):
    """Общий список игроков за сезон"""
    player_scores = Statistic.objects.filter(
        season__name=season).values(
            'name__id', 'name__name', 'age').annotate(
                team=StringAgg('team__slug', delimiter=','),
                game=Sum('game'),
                goal=Sum('goal'),
                assist=Sum('assist'),
                point=Sum('point'),
                penalty=Sum('penalty')).order_by(
                    f'-{stat_rule}', '-goal', 'game')[:54]
    template = 'posts/best_of_season.html'
    context = {
        'season': season,
        'previous_season': prev_next_season(season)[1],
        'next_season': prev_next_season(season)[0],
        'page_obj': player_scores,
        'stat_rule': stat_rule
    }
    return render(request, template, context)


def all_time_all_player_one_team(request, team):
    """все игроки выступавшие за одну команду за все время"""
    total_points_for_players = Statistic.objects.filter(
        team__title=team).values(
            'name__id',
            'name__name').annotate(
            games=Sum('game'),
            goals=Sum('goal'),
            assists=Sum('assist'),
            points=Sum('point'),
            penalty=Sum('penalty')).order_by(
                '-points', '-goals', 'games')
    template = 'posts/all_time_all_player_one_team.html'
    context = {
        'page_obj': total_points_for_players,
        'team': team,
        'top_goal': top_goal(team),
        'top_point': top_point(team),
        'top_s_goal': top_season_goal(team),
        'top_s_point': top_season_point(team),
    }
    return render(request, template, context)


def statistic(request, stat_rule):
    """фнкция позволяющая получить сортированный список игроков
    по ключевым статистическим показателям"""
    rule = stat_rule.split('_')
    if rule[1] == 'career':
        total_for_players = Statistic.objects.values(
            'name__id',
            'name__name'
        ).annotate(
            game=Sum('game'),
            goal=Sum('goal'),
            assist=Sum('assist'),
            point=Sum('point'),
            penalty=Sum('penalty')
        ).order_by(
            f'-{rule[0]}',
            'game'
        )[:50]
        context = {
            'page_obj': total_for_players,
            'table_name': 'Career Leaders for' + ' ' + f'{rule[0].title()}''s'
        }
    elif rule[1] == 'season':
        total_for_players = Statistic.objects.values(
            'name__id',
            'name__name',
            'season__name'
        ).annotate(
            game=Sum('game'),
            goal=Sum('goal'),
            assist=Sum('assist'),
            point=Sum('point'),
            penalty=Sum('penalty')
        ).order_by(
            f'-{rule[0]}',
            'game'
        )[:50]
        context = {
            'page_obj': total_for_players,
            'table_name':
            'Single Season Leaders for' + ' ' + f'{rule[0].title()}''s'
        }
    template = 'posts/index.html'
    return render(request, template, context)


def create_table(request, season):
    """функция получения турнирных таблиц и короткого списка лучших
    игроков для конкретного сезона"""
    teams = TeamForTable.objects.filter(season__name=season).order_by('rank')
    teams2round = TeamForTable2Round.objects.all().filter(
        season__name=season).order_by('rank')
    playoff = Playoff.objects.filter(season__name=season).order_by('number')
    top_player = Statistic.objects.filter(
        season__name=season)
    top_5_point = top_player.values(
        'name__id',
        'name__name',
        'team__slug').annotate(
            game=Sum('game'),
            point=Sum('point')).order_by('-point', 'goal')[:5]
    top_5_goal = top_player.values(
        'name__id',
        'name__name',
        'team__slug').annotate(
            game=Sum('game'),
            goal=Sum('goal')).order_by('-goal', 'game')[:5]
    top_5_assist = top_player.values(
        'name__id',
        'name__name',
        'team__slug').annotate(
            game=Sum('game'),
            assist=Sum('assist')).order_by('-assist', 'game')[:5]
    top_5_penalty = top_player.values(
        'name__id',
        'name__name',
        'team__slug').annotate(
            game=Sum('game'),
            penalty=Sum('penalty')).order_by('-penalty', 'game')[:5]
    template = 'table/teams_table.html'
    context = {
        'previous_season': prev_next_season(season)[1],
        'next_season': prev_next_season(season)[0],
        'page_obj': teams,
        'teams2round': teams2round,
        'playoff': playoff,
        'season': season,
        'top_5': top_5_point,
        'top_5_goal': top_5_goal,
        'top_5_assist': top_5_assist,
        'top_5_penalty': top_5_penalty,
    }
    return render(request, template, context)


def leaders_career(request, team):
    """Десятка лучших по основным показателям за карьеру
    в команде"""
    query_list = Statistic.objects.filter(
        team__title=team).values(
            'name__id',
            'name__name').annotate(
                game=Sum('game'),
                goal=Sum('goal'),
                assist=Sum('assist'),
                penalty=Sum('penalty'))
    top_10_game = query_list.order_by('-game')[:10]
    top_10_goal = query_list.order_by('-goal')[:10]
    top_10_assist = query_list.order_by('-assist')[:10]
    top_10_penalty = query_list.order_by('-penalty')[:10]
    context = {
        'top_10_game': top_10_game,
        'top_10_goal': top_10_goal,
        'top_10_assist': top_10_assist,
        'top_10_penalty': top_10_penalty,
        'team': team,
        'top_goal': top_goal(team),
        'top_point': top_point(team),
        'top_s_goal': top_season_goal(team),
        'top_s_point': top_season_point(team)
    }
    template = 'posts/leaders_career.html'
    return render(request, template, context)


def season_leaders(request, team):
    """10 лучших результатов за сезон в команде"""
    query_list = Statistic.objects.filter(
        team__title=team).values(
            'name__id',
            'name__name',
            'season__name').annotate(
                goal=Sum('goal'),
                assist=Sum('assist'),
                point=Sum('point'),
                penalty=Sum('penalty'))
    top_10_goal = query_list.order_by('-goal')[:10]
    top_10_assist = query_list.order_by('-assist')[:10]
    top_10_point = query_list.order_by('-point')[:10]
    top_10_penalty = query_list.order_by('-penalty')[:10]
    context = {
        'top_10_goal': top_10_goal,
        'top_10_assist': top_10_assist,
        'top_10_point': top_10_point,
        'top_10_penalty': top_10_penalty,
        'team': team,
        'top_goal': top_goal(team),
        'top_point': top_point(team),
        'top_s_goal': top_season_goal(team),
        'top_s_point': top_season_point(team)
    }
    template = 'posts/season_leaders.html'
    return render(request, template, context)


def history_team(request, team):
    """ функция формирования содержимого страницы с историей команды """
    team_view = TeamForTable.objects.filter(
        name__title=team).select_related(
            'round_2', 'playoff').order_by('-season__name')
    count_season = team_view.count()
    context = {
        'team_view': team_view,
        'team': team,
        'count_season': count_season,
        'top_goal': top_goal(team),
        'top_point': top_point(team),
        'top_s_goal': top_season_goal(team),
        'top_s_point': top_season_point(team)
    }
    template = 'posts/history_team.html'
    return render(request, template, context)


class SearchResultsView(ListView):
    """поиск, в виде эксперимента через класс"""
    model = Player
    template_name = 'search/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Player.objects.filter(
            Q(name__icontains=query.title()) | Q(
                year_of_birth__icontains=query)
        ).order_by('name')
