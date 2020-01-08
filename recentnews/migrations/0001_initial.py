# Generated by Django 2.2.4 on 2020-01-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatchDetails',
            fields=[
                ('matchid', models.IntegerField(primary_key=True, serialize=False)),
                ('srs', models.CharField(max_length=1000)),
                ('mnum', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('mchstate', models.CharField(max_length=100)),
                ('status', models.TextField()),
                ('venue_name', models.TextField()),
                ('venue_location', models.TextField()),
                ('toss', models.CharField(max_length=1000)),
                ('date_modified_md', models.DateTimeField(verbose_name='MatchDetails Modified on')),
            ],
        ),
        migrations.CreateModel(
            name='Recentnews',
            fields=[
                ('newsid', models.AutoField(primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=750)),
                ('upload_time', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='TeamDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name1', models.CharField(max_length=100)),
                ('runs1', models.CharField(max_length=100)),
                ('wickets1', models.CharField(max_length=12)),
                ('overs1', models.CharField(max_length=100)),
                ('inning_num1', models.CharField(default='1', max_length=4)),
                ('team_name2', models.CharField(max_length=100)),
                ('runs2', models.CharField(default=None, max_length=100)),
                ('wickets2', models.CharField(default=None, max_length=12)),
                ('overs2', models.CharField(default=None, max_length=100)),
                ('inning_num2', models.CharField(default='2', max_length=4)),
                ('team_name3', models.CharField(max_length=100)),
                ('runs3', models.CharField(default=None, max_length=100)),
                ('wickets3', models.CharField(default=None, max_length=12)),
                ('overs3', models.CharField(default=None, max_length=100)),
                ('inning_num3', models.CharField(default='3', max_length=4)),
                ('team_name4', models.CharField(max_length=100)),
                ('runs4', models.CharField(default=None, max_length=100)),
                ('wickets4', models.CharField(default=None, max_length=12)),
                ('overs4', models.CharField(default=None, max_length=100)),
                ('inning_num4', models.CharField(default='3', max_length=4)),
                ('date_modified_td', models.DateTimeField(verbose_name='TeamDetails Modified on')),
                ('matchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recentnews.MatchDetails')),
            ],
        ),
    ]
