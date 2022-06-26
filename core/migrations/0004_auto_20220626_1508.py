# Generated by Django 3.2.13 on 2022-06-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_plato_patente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descuento', models.IntegerField(null=True)),
                ('imagen', models.CharField(blank=True, max_length=400, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Plato',
        ),
    ]
