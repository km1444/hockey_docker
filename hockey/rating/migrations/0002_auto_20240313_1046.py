# Generated by Django 2.2.16 on 2024-03-13 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalkeeperStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.SmallIntegerField(default=14, verbose_name='Возраст')),
                ('game', models.SmallIntegerField(default=1, verbose_name='Игры')),
                ('goal_against', models.SmallIntegerField(default=0, verbose_name='Голы')),
                ('penalty', models.SmallIntegerField(default=0, verbose_name='Штраф')),
            ],
            options={
                'verbose_name': 'Статистика Вратаря',
                'verbose_name_plural': 'Статистика Вратарей',
                'ordering': ('-season',),
            },
        ),
        migrations.CreateModel(
            name='PersonRound2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='golkeeperstatistic',
            name='name',
        ),
        migrations.RemoveField(
            model_name='golkeeperstatistic',
            name='position',
        ),
        migrations.RemoveField(
            model_name='golkeeperstatistic',
            name='season',
        ),
        migrations.RemoveField(
            model_name='golkeeperstatistic',
            name='team',
        ),
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ('-season',), 'verbose_name': 'Статистика полевого игрока', 'verbose_name_plural': 'Статистика полевых игроков'},
        ),
        migrations.RemoveField(
            model_name='teamfortable',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='teamfortable2',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='teamfortable3',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='teamfortable4',
            name='coach',
        ),
        migrations.AddField(
            model_name='player',
            name='wikip',
            field=models.URLField(blank=True, max_length=250, verbose_name='Ссылка на википедию'),
        ),
        migrations.AddField(
            model_name='team',
            name='emblem',
            field=models.ImageField(blank=True, upload_to='emblem/', verbose_name='Эмблема'),
        ),
        migrations.AddField(
            model_name='teamfortable',
            name='coach_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables_coach_1', to='rating.Player', verbose_name='Тренер'),
        ),
        migrations.AddField(
            model_name='teamfortable',
            name='coach_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables_coach_2', to='rating.Player', verbose_name='Тренер_2'),
        ),
        migrations.AddField(
            model_name='teamfortable',
            name='coach_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables_coach_3', to='rating.Player', verbose_name='Тренер_3'),
        ),
        migrations.AddField(
            model_name='teamfortable2',
            name='coach_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables2_coach_1', to='rating.Player', verbose_name='Тренер'),
        ),
        migrations.AddField(
            model_name='teamfortable2',
            name='coach_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables2_coach_2', to='rating.Player', verbose_name='Тренер_2'),
        ),
        migrations.AddField(
            model_name='teamfortable2',
            name='coach_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables2_coach_3', to='rating.Player', verbose_name='Тренер_3'),
        ),
        migrations.AddField(
            model_name='teamfortable3',
            name='coach_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables3_coach_1', to='rating.Player', verbose_name='Тренер'),
        ),
        migrations.AddField(
            model_name='teamfortable3',
            name='coach_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables3_coach_2', to='rating.Player', verbose_name='Тренер_2'),
        ),
        migrations.AddField(
            model_name='teamfortable3',
            name='coach_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables3_coach_3', to='rating.Player', verbose_name='Тренер_3'),
        ),
        migrations.AddField(
            model_name='teamfortable4',
            name='coach_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables4_coach_1', to='rating.Player', verbose_name='Тренер'),
        ),
        migrations.AddField(
            model_name='teamfortable4',
            name='coach_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables4_coach_2', to='rating.Player', verbose_name='Тренер_2'),
        ),
        migrations.AddField(
            model_name='teamfortable4',
            name='coach_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables4_coach_3', to='rating.Player', verbose_name='Тренер_3'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.TextField(verbose_name='Игрок'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='rating.Season', verbose_name='Сезон'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='rating.Team', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='teamfortable',
            name='round_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables', to='rating.PersonRound2'),
        ),
        migrations.AlterField(
            model_name='teamfortable2',
            name='round_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables2', to='rating.PersonRound2'),
        ),
        migrations.AlterField(
            model_name='teamfortable3',
            name='round_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables3', to='rating.PersonRound2'),
        ),
        migrations.AlterField(
            model_name='teamfortable4',
            name='round_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_for_tables4', to='rating.PersonRound2'),
        ),
        migrations.AddConstraint(
            model_name='statistic',
            constraint=models.UniqueConstraint(fields=('name', 'team', 'season'), name='unique_statistic'),
        ),
        migrations.DeleteModel(
            name='GolkeeperStatistic',
        ),
        migrations.AddField(
            model_name='personround2',
            name='table1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.TeamForTable2Round', verbose_name=''),
        ),
        migrations.AddField(
            model_name='personround2',
            name='table2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.TeamForTable2Round2', verbose_name=''),
        ),
        migrations.AddField(
            model_name='personround2',
            name='table3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.TeamForTable2Round3', verbose_name=''),
        ),
        migrations.AddField(
            model_name='goalkeeperstatistic',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goalkeeperstatistic', to='rating.Player', verbose_name='Игрок'),
        ),
        migrations.AddField(
            model_name='goalkeeperstatistic',
            name='position',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goalkeeperstatistic', to='rating.Position', verbose_name='Позиция'),
        ),
        migrations.AddField(
            model_name='goalkeeperstatistic',
            name='season',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, related_name='goalkeeperstatistic', to='rating.Season', verbose_name='Сезон'),
        ),
        migrations.AddField(
            model_name='goalkeeperstatistic',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='goalkeeperstatistic', to='rating.Team', verbose_name='Команда'),
        ),
        migrations.AddConstraint(
            model_name='goalkeeperstatistic',
            constraint=models.UniqueConstraint(fields=('name', 'team', 'season'), name='unique_goalkeeper_statistic'),
        ),
    ]
