# Generated by Django 2.2.8 on 2021-03-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20191216_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=200, verbose_name='Indica una dirección postal precisa')),
                ('route', models.CharField(blank=True, max_length=150, null=True, verbose_name='Indica una ruta con nombre')),
                ('point_of_interest', models.CharField(blank=True, max_length=150, null=True, verbose_name='Indica un punto de interés con nombre')),
                ('park', models.CharField(blank=True, max_length=150, null=True, verbose_name='Parque cercano')),
                ('airport', models.CharField(blank=True, max_length=150, null=True, verbose_name='Aeropuerto cercano')),
                ('natural_feature', models.CharField(blank=True, max_length=150, null=True, verbose_name='indica una característica natural prominente')),
                ('postal_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='Código postal')),
                ('plus_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='Referencia de ubicación codificada(Plus code)')),
                ('neighborhood', models.CharField(blank=True, max_length=150, null=True, verbose_name='Vecindario')),
                ('locality', models.CharField(blank=True, max_length=150, null=True, verbose_name='Localidad')),
                ('sublocality', models.CharField(blank=True, max_length=150, null=True, verbose_name='Entidad civil de primer orden debajo de una localidad')),
                ('colloquial_area', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre de uso común para la entidad')),
                ('administrative_area_level_1', models.CharField(blank=True, max_length=150, null=True, verbose_name='Entidad civil por debajo del nivel de país')),
                ('administrative_area_level_2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Entidad civil por debajo del nivel de país')),
                ('country', models.CharField(blank=True, max_length=150, null=True, verbose_name='Indica la entidad política nacional')),
                ('political', models.CharField(blank=True, max_length=150, null=True, verbose_name='entidad política')),
                ('is_fiscal', models.BooleanField(default=False, verbose_name='¿Es una dirección fiscal?')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Dirección',
            },
        ),
    ]
