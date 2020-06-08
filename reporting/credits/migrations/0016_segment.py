# Generated by Django 3.0.6 on 2020-06-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0015_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=2)),
                ('NAME', models.CharField(choices=[('Прочие', 'Прочие'), ('ФЛ', 'ФЛ'), ('Торговля', 'Торговля')], max_length=255)),
            ],
        ),
    ]