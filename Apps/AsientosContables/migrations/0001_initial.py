# Generated by Django 3.0 on 2019-12-07 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empleados', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
                ('Monto', models.FloatField()),
                ('CodigoAuxiliar', models.PositiveIntegerField(default=0)),
                ('NaturalezaCuenta', models.CharField(choices=[('DB', 'Debito'), ('CR', 'Credito')], default='DB', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='AsientoContable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
                ('FechaAsiento', models.DateTimeField(auto_now_add=True)),
                ('Estado', models.CharField(choices=[('R', 'Registrado'), ('P', 'Pendiente')], default='P', max_length=2)),
                ('IDauxiliar', models.PositiveIntegerField(default=2)),
                ('Moneda', models.CharField(choices=[('1', 'DOP'), ('2', 'Dolar')], default='1', max_length=2)),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.Empleado')),
            ],
        ),
    ]