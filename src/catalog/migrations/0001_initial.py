# Generated by Django 3.2.9 on 2021-11-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='ФИО')),
                ('position', models.CharField(max_length=40, verbose_name='Должность')),
                ('recruitment_date', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Размер заработной платы')),
                ('payd_salary', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Выплаченная заработная плата')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
