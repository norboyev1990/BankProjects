# Generated by Django 3.0.6 on 2020-06-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0007_auto_20200604_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdata',
            name='DATE_DOGOVOR',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='DATE_FACTUAL',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='DATE_OBRAZ_PROS',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='DATE_POGASH',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='DATE_POGASH_POSLE_PRODL',
            field=models.DateField(null=True),
        ),
    ]