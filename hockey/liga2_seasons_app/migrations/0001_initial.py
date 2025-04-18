# Generated by Django 2.2.16 on 2025-04-12 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место')),
                ('current_name', models.CharField(max_length=50, verbose_name='Текущее название')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_add_tables', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_add_tables', to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Команда дополнителного турнира',
                'verbose_name_plural': 'Команды дополнительного турнира',
            },
        ),
        migrations.CreateModel(
            name='AdditionalTournamentSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место')),
                ('current_name', models.CharField(max_length=50, verbose_name='Текущее название')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_add_tables_2', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_add_tables_2', to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Команда второго дополнителного турнира',
                'verbose_name_plural': 'Команды второго дополнительного турнира',
            },
        ),
        migrations.CreateModel(
            name='AdditionalTournamentWithoutPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место')),
                ('current_name', models.CharField(max_length=50, verbose_name='Текущее название')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_tournament_without_points', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_tournament_without_points', to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Команда доп т-ра без учета набранных ранее очков',
                'verbose_name_plural': 'Команды доп т-ра без учета набранных ранее очков',
            },
        ),
        migrations.CreateModel(
            name='TransitionWithoutPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место в таблице')),
                ('current_name', models.CharField(max_length=50, verbose_name='Текущее имя')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='without_points', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Команда переходного турнира без ранее набранных очков',
                'verbose_name_plural': 'Команды переходного турнира без ранее набранных очков',
            },
        ),
        migrations.CreateModel(
            name='TransitionTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_real', models.IntegerField(verbose_name='Место для формирования таблицы')),
                ('rank_pict', models.IntegerField(verbose_name='Место выводимое на экран')),
                ('current_name', models.CharField(max_length=50, verbose_name='Текущее имя')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_transtour', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Команда переходного турнира',
                'verbose_name_plural': 'Команды переходного турнира',
            },
        ),
        migrations.CreateModel(
            name='TransitionSerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_1', models.CharField(max_length=10, verbose_name='Счет матча 1')),
                ('game_2', models.CharField(max_length=10, verbose_name='Счет матча 2')),
                ('game_3', models.CharField(max_length=10, verbose_name='Счет матча 3')),
                ('game_4', models.CharField(max_length=10, verbose_name='Счет матча 4')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1_in_transserie', to='rating.Team', verbose_name='Команда')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2_in_transserie', to='rating.Team', verbose_name='Команда')),
            ],
        ),
        migrations.CreateModel(
            name='TeamInTable2gr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место')),
                ('current_name', models.CharField(blank=True, max_length=50, verbose_name='Текущее название')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('additional_tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.AdditionalTournament', verbose_name='Участие в доп.турнире')),
                ('additional_tournament_second', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.AdditionalTournamentSecond', verbose_name='Участие во втором доп.турнире')),
                ('additional_tournament_without_points', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.AdditionalTournamentWithoutPoints', verbose_name='Участие в доп т-ре без учета ранее набранных очков')),
                ('coach_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_2_tables_coach_1', to='rating.Player', verbose_name='Тренер')),
                ('coach_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_2_tables_coach_2', to='rating.Player', verbose_name='Тренер_2')),
                ('coach_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_2_tables_coach_3', to='rating.Player', verbose_name='Тренер_3')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_2_tables', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_2_tables', to='rating.Team', verbose_name='Команда')),
                ('transition_serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.TransitionSerie', verbose_name='Участие в переходной серии')),
                ('transition_tournament', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.TransitionTournament', verbose_name='Участие в переходном турнире')),
                ('transition_tournament_without_points', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.TransitionWithoutPoints', verbose_name='Участие в перех т-ре без учета ранее набранных очков')),
            ],
            options={
                'verbose_name': 'Команда второй группы',
                'verbose_name_plural': 'Команды второй группы',
                'ordering': ('season__name',),
            },
        ),
        migrations.CreateModel(
            name='TeamInTable1gr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Место')),
                ('current_name', models.CharField(blank=True, max_length=50, verbose_name='Текущее название')),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('additional_tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.AdditionalTournament', verbose_name='Участие в доп.турнире')),
                ('additional_tournament_second', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.AdditionalTournamentSecond', verbose_name='Участие во втором доп.турнире')),
                ('additional_tournament_without_points', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.AdditionalTournamentWithoutPoints', verbose_name='Участие в доп т-ре без учета ранее набранных очков')),
                ('coach_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_tables_coach_1', to='rating.Player', verbose_name='Тренер')),
                ('coach_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_tables_coach_2', to='rating.Player', verbose_name='Тренер_2')),
                ('coach_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_tables_coach_3', to='rating.Player', verbose_name='Тренер_3')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_in_tables', to='rating.Season', verbose_name='Сезон')),
                ('team_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_in_tables', to='rating.Team', verbose_name='Команда')),
                ('transition_serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liga2_seasons_app.TransitionSerie', verbose_name='Участие в переходной серии')),
                ('transition_tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.TransitionTournament', verbose_name='Участие в переходном турнире')),
                ('transition_tournament_without_points', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='liga2_seasons_app.TransitionWithoutPoints', verbose_name='Участие в перех т-ре без учета ранее набранных очков')),
            ],
            options={
                'verbose_name': 'Команда 1 группы',
                'verbose_name_plural': 'Команды 1 группы',
                'ordering': ('season__name',),
            },
        ),
        migrations.CreateModel(
            name='DescriptionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition_tournament', models.CharField(blank=True, max_length=50, verbose_name='Переходный турнир')),
                ('description_1tb', models.CharField(blank=True, max_length=50, verbose_name='Основной турнир или Запад')),
                ('description_2tb', models.CharField(blank=True, max_length=50, verbose_name='Дополнительный турнир')),
                ('description_3tb', models.CharField(blank=True, max_length=50, verbose_name='Второй доп турнир')),
                ('description_4tb', models.CharField(blank=True, max_length=50, verbose_name='Восток')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description_table_liga2', to='rating.Season', verbose_name='Сезон')),
            ],
        ),
    ]
