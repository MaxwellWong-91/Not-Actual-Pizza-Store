# Generated by Django 3.0 on 2019-12-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaType', models.BooleanField(default=True)),
                ('size', models.CharField(choices=[('SM', 'SMALL'), ('LG', 'LARGE')], default='SM', max_length=2)),
                ('toppings', models.ManyToManyField(to='orders.Topping')),
            ],
        ),
    ]
