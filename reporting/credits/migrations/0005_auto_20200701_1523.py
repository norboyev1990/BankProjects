# Generated by Django 3.0.7 on 2020-07-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0004_auto_20200630_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempdata',
            old_name='NUMBER',
            new_name='NUMBERS',
        ),
        migrations.AlterField(
            model_name='tempdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]