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
            name='CoachStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.SmallIntegerField(default=14, verbose_name='Возраст')),
                ('final_position', models.SmallIntegerField(blank=True, null=True)),
                ('full_season', models.BooleanField(default=True)),
                ('fired_season', models.BooleanField(default=False)),
                ('came_season', models.BooleanField(default=False)),
                ('coach_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coachstatistic', to='rating.Player', verbose_name='Тренер')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coachstatistic', to='rating.Season', verbose_name='Сезон')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coachstatistic', to='rating.Team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Статистика тренера',
                'verbose_name_plural': 'Статистика тренеров',
                'ordering': ('-season',),
            },
        ),
    ]
