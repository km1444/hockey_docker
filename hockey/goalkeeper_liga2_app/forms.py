from django import forms
from rating.models import Player, Season, Team

from .models import GoalkeeperStatisticLiga2


class AddGoalkeeperStatisticLiga2Form(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        label='Команда'
    )
    season = forms.ModelChoiceField(
        queryset=Season.objects.all(),
        label='Сезон'
    )
    name = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        label='Игрок'
    )

    class Meta:
        model = GoalkeeperStatisticLiga2
        fields = (
            'name', 'team', 'season', 'position',
            'game', 'goal_against', 'penalty'
        )


class EditGoalkeeperStatLiga2Form(forms.ModelForm):
    class Meta:
        model = GoalkeeperStatisticLiga2
        fields = (
            'name', 'position',
            'game', 'goal_against', 'penalty'
        )
