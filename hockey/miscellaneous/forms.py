from django import forms
from rating.models import Season


class FilterForm(forms.ModelForm):
    stat_types = (
        ('goal', 'goal'),
        ('game', 'game'),
        ('assist', 'assist'),
        ('point', 'point'),
    )
    name = forms.ModelChoiceField(
        queryset=Season.objects.all().order_by('name'),
        label='Начало'
    )
    name2 = forms.ModelChoiceField(
        queryset=Season.objects.all().order_by('name'),
        label='Конец'
    )
    types = forms.ChoiceField(
        choices=stat_types, label='Вариант')

    class Meta:
        model = Season
        fields = (
            'name',
        )
