# Generated by Django 3.0 on 2019-12-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20191226_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=5),
        ),
        migrations.AlterField(
            model_name='platters',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=5),
        ),
        migrations.AlterField(
            model_name='subs',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=5),
        ),
    ]
