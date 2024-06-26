# Generated by Django 5.0.6 on 2024-06-09 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competencies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('competency_name', models.CharField(max_length=100)),
                ('competency_definition', models.TextField()),
                ('competency_type', models.CharField(choices=[('technical', 'Technical'), ('organizational', 'Organizational')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceIndicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompetenciesProfiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert/Leader', 'Expert/Leader')], max_length=20)),
                ('competency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance_indicator.competencies')),
                ('performance_indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance_indicator.performanceindicator')),
            ],
        ),
    ]
