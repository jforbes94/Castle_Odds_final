# Generated by Django 4.0.4 on 2022-05-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestOdds',
            fields=[
                ('game_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('away_team', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('sport_key', models.CharField(max_length=100)),
                ('sport_title', models.CharField(max_length=100)),
                ('SportsbookH2H_home_price1', models.CharField(max_length=100)),
                ('H2H_home_price1', models.CharField(max_length=100)),
                ('SportsbookH2H_home_price2', models.CharField(max_length=100)),
                ('H2H_home_price2', models.CharField(max_length=100)),
                ('SportsbookH2H_home_price3', models.CharField(max_length=100)),
                ('H2H_home_price3', models.CharField(max_length=100)),
                ('SportsbookH2H_away_price1', models.CharField(max_length=100)),
                ('H2H_away_price1', models.CharField(max_length=100)),
                ('SportsbookH2H_away_price2', models.CharField(max_length=100)),
                ('H2H_away_price2', models.CharField(max_length=100)),
                ('SportsbookH2H_away_price3', models.CharField(max_length=100)),
                ('H2H_away_price3', models.CharField(max_length=100)),
                ('Sportsbook_spread_home_price1', models.CharField(max_length=100)),
                ('spread_home_price1', models.CharField(max_length=100)),
                ('home_spread1', models.CharField(max_length=100)),
                ('Sportsbook_spread_home_price2', models.CharField(max_length=100)),
                ('spread_home_price2', models.CharField(max_length=100)),
                ('home_spread2', models.CharField(max_length=100)),
                ('Sportsbook_spread_home_price3', models.CharField(max_length=100)),
                ('spread_home_price3', models.CharField(max_length=100)),
                ('home_spread3', models.CharField(max_length=100)),
                ('Sportsbook_spread_away_price1', models.CharField(max_length=100)),
                ('spread_away_price1', models.CharField(max_length=100)),
                ('away_spread1', models.CharField(max_length=100)),
                ('Sportsbook_spread_away_price2', models.CharField(max_length=100)),
                ('spread_away_price2', models.CharField(max_length=100)),
                ('away_spread2', models.CharField(max_length=100)),
                ('Sportsbook_spread_away_price3', models.CharField(max_length=100)),
                ('spread_away_price3', models.CharField(max_length=100)),
                ('away_spread3', models.CharField(max_length=100)),
                ('Sportsbook_over_price1', models.CharField(max_length=100)),
                ('over_price1', models.CharField(max_length=100)),
                ('over1', models.CharField(max_length=100)),
                ('Sportsbook_over_price2', models.CharField(max_length=100)),
                ('over_price2', models.CharField(max_length=100)),
                ('over2', models.CharField(max_length=100)),
                ('Sportsbook_over_price3', models.CharField(max_length=100)),
                ('over_price3', models.CharField(max_length=100)),
                ('over3', models.CharField(max_length=100)),
                ('Sportsbook_under_price1', models.CharField(max_length=100)),
                ('under_price1', models.CharField(max_length=100)),
                ('under1', models.CharField(max_length=100)),
                ('Sportsbook_under_price2', models.CharField(max_length=100)),
                ('under_price2', models.CharField(max_length=100)),
                ('under2', models.CharField(max_length=100)),
                ('Sportsbook_under_price3', models.CharField(max_length=100)),
                ('under_price3', models.CharField(max_length=100)),
                ('under3', models.CharField(max_length=100)),
                ('H2H_home_price1_ST', models.CharField(max_length=100)),
                ('H2H_home_price2_ST', models.CharField(max_length=100)),
                ('H2H_home_price3_ST', models.CharField(max_length=100)),
                ('H2H_away_price1_ST', models.CharField(max_length=100)),
                ('H2H_away_price2_ST', models.CharField(max_length=100)),
                ('H2H_away_price3_ST', models.CharField(max_length=100)),
                ('spread_home_price1_ST', models.CharField(max_length=100)),
                ('spread_home_price2_ST', models.CharField(max_length=100)),
                ('spread_home_price3_ST', models.CharField(max_length=100)),
                ('spread_away_price1_ST', models.CharField(max_length=100)),
                ('spread_away_price2_ST', models.CharField(max_length=100)),
                ('spread_away_price3_ST', models.CharField(max_length=100)),
                ('over_price1_ST', models.CharField(max_length=100)),
                ('over_price2_ST', models.CharField(max_length=100)),
                ('over_price3_ST', models.CharField(max_length=100)),
                ('under_price1_ST', models.CharField(max_length=100)),
                ('under_price2_ST', models.CharField(max_length=100)),
                ('under_price3_ST', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sports',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('away_team', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('sport_key', models.CharField(max_length=100)),
                ('sport_title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='Odds',
            fields=[
                ('game_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('away_team', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('sport_key', models.CharField(max_length=100)),
                ('sport_title', models.CharField(max_length=100)),
                ('sportsbook', models.CharField(max_length=200)),
                ('last_update', models.CharField(max_length=200)),
                ('H2H_home_price', models.CharField(max_length=100)),
                ('H2H_away_price', models.CharField(max_length=100)),
                ('home_spread', models.CharField(max_length=100)),
                ('away_spread', models.CharField(max_length=100)),
                ('spread_home_price', models.CharField(max_length=100)),
                ('spread_away_price', models.CharField(max_length=100)),
                ('over', models.CharField(max_length=100)),
                ('under', models.CharField(max_length=100)),
                ('over_price', models.CharField(max_length=100)),
                ('under_price', models.CharField(max_length=100)),
            ],
        ),
    ]
