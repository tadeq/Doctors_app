# Generated by Django 2.0.5 on 2018-06-14 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr', models.TimeField()),
                ('to', models.TimeField()),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(default='2018-06-14')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='workday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schedule.Workday'),
        ),
    ]
