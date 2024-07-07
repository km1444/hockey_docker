# from itertools import chain

from liga2_seasons_app.models import TeamInTable1gr


def all_team(request):
    all_team_liga2_1 = TeamInTable1gr.objects.values(
        'team_name__title',
        'team_name__city'
    ).order_by('team_name__title').distinct()
    # all_team_liga2_2 = TeamInTable2gr.objects.values(
    #     'team_name__title',
    #     'team_name__city'
    # ).order_by('team_name__title').distinct()
    return {
        'all_team_liga2': all_team_liga2_1
    }
