from django import forms
from rating.models import Player, Season, Team

from .models import StatisticPlayer


class AddStatisticLiga2Form(forms.ModelForm):
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
        model = StatisticPlayer
        fields = (
            'name', 'team', 'season', 'position',
            'game', 'goal', 'assist', 'penalty'
        )
        widgets = {
        }


class EditStatisticLiga2Form(forms.ModelForm):
    class Meta:
        model = StatisticPlayer
        fields = (
            'name', 'position',
            'game', 'goal', 'assist', 'penalty'
        )
