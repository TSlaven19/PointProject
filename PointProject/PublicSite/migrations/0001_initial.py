# Generated by Django 2.1.5 on 2019-02-09 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_scoree', models.CharField(choices=[('AMK', 'Annaleise'), ('TDS', 'Tobin'), ('BTH', 'Both')], default='BTH', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.CharField(max_length=200)),
                ('point_value', models.SmallIntegerField(default=0)),
                ('point_cooldown', models.SmallIntegerField(default=0)),
                ('point_active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PublicSite.Point'),
        ),
    ]
