# Generated by Django 4.0.6 on 2022-07-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('ValueId', models.AutoField(primary_key=True, serialize=False)),
                ('USD', models.IntegerField(max_length=500)),
                ('EUR', models.IntegerField(max_length=500)),
                ('ETH', models.IntegerField(max_length=500)),
                ('BTC', models.IntegerField(max_length=500)),
                ('BRL', models.IntegerField(max_length=500)),
            ],
            options={
                'verbose_name': 'Valuer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('CurrencyId', models.AutoField(primary_key=True, serialize=False)),
                ('LastUpdDate', models.DateTimeField(max_length=500)),
                ('Value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency_exchanger.value')),
            ],
            options={
                'verbose_name': 'Currency',
                'managed': True,
            },
        ),
    ]
