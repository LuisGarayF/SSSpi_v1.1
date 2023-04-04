# Generated by Django 4.2 on 2023-04-04 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customer_email', models.EmailField(max_length=254, null=True, verbose_name='Correo Electrónico')),
                ('customer_name', models.CharField(max_length=64, verbose_name='Nombre')),
                ('subject', models.CharField(max_length=255, verbose_name='Asunto')),
                ('message', models.TextField(max_length=1000, verbose_name='Mensaje')),
            ],
            options={
                'db_table': 'contactform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplicacion', models.CharField(blank=True, db_column='aplicacion', max_length=100, null=True, verbose_name='Aplicación Industrial')),
            ],
            options={
                'verbose_name_plural': 'Aplicaciones',
                'db_table': 'aplicacion',
            },
        ),
        migrations.CreateModel(
            name='Combustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustible', models.CharField(max_length=300, verbose_name='combustible')),
            ],
            options={
                'verbose_name_plural': 'combustibles',
                'db_table': 'combustible',
            },
        ),
        migrations.CreateModel(
            name='Esquema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esquema', models.CharField(blank=True, default='Campo solar y caldera en serie con recirculación desde caldera', max_length=200, verbose_name='Esquema de integración')),
                ('siglas_esquema', models.CharField(default='SL_L_PD', max_length=20, verbose_name='Siglas esquema Integration')),
                ('imagen_esquema', models.FileField(upload_to='./static/img/esquemas_integracion/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'esquema de integración',
                'verbose_name_plural': 'esquemas de integración',
                'db_table': 'esquema_integracion',
            },
        ),
        migrations.CreateModel(
            name='Inicio_Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ini_jornada', models.CharField(default='00:00', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Inicio Jornadas',
                'db_table': 'inicio_jornada',
            },
        ),
        migrations.CreateModel(
            name='Material_Aislamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_aislamiento', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Material Aislamiento',
                'verbose_name_plural': 'Materiales Aislamiento',
                'db_table': 'material_aislacion',
            },
        ),
        migrations.CreateModel(
            name='Material_Almacenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_almacenamiento', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Material Almacenamiento',
                'verbose_name_plural': 'Materiales Almacenamiento',
                'db_table': 'material_almacenamiento',
            },
        ),
        migrations.CreateModel(
            name='Relacion_Aspecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacion_aspecto', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Relación de Aspecto',
                'verbose_name_plural': 'Relaciones de Aspecto',
                'db_table': 'relacion_aspecto',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(db_column='sector', max_length=100, verbose_name='Sector Industrial')),
            ],
            options={
                'verbose_name_plural': 'Sectores',
                'db_table': 'sector',
            },
        ),
        migrations.CreateModel(
            name='Tabla_colectores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('numero_srcc', models.CharField(blank=True, max_length=200)),
                ('tipo', models.CharField(blank=True, max_length=200)),
                ('fluido_prueba', models.PositiveIntegerField()),
                ('rango_flujo_prueba', models.FloatField()),
                ('area', models.FloatField()),
                ('frta', models.FloatField()),
                ('frul', models.FloatField()),
                ('iam', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tabla de colectores',
                'verbose_name_plural': 'Tabla de colectores',
                'db_table': 'tabla_colectores',
            },
        ),
        migrations.CreateModel(
            name='Termino_Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_jornada', models.CharField(default='23:30', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Término Jornadas',
                'db_table': 'termino_jornada',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Caldera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_caldera', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Caldera',
                'verbose_name_plural': 'Tipos de Caldera',
                'db_table': 'tipo_caldera',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Fluido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_fluido', models.CharField(default='Agua', max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo Fluido',
                'verbose_name_plural': 'Tipos de Fluidos',
                'db_table': 'tipo_fluido',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ubicacion', models.CharField(max_length=100, verbose_name='Ubicación')),
                ('latitud', models.FloatField(max_length=50, verbose_name='Latitud')),
                ('longitud', models.FloatField(max_length=50, verbose_name='Longitud')),
            ],
            options={
                'verbose_name_plural': 'Ubicaciones',
                'db_table': 'ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Costo_Combustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_costo_combustible', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Unidad Costo Combustible',
                'verbose_name_plural': 'Unidades Costo Combustible',
                'db_table': 'costo_combustible',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Demanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_demanda', models.CharField(max_length=300, verbose_name='unidad_demanda')),
            ],
            options={
                'verbose_name_plural': 'Unidades demanda',
                'db_table': 'unidad_demanda',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Flujo_Masico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_flujo_masico', models.CharField(default='kg/s', max_length=20, verbose_name='Unidad flujo másico')),
            ],
            options={
                'verbose_name': 'Unidad Flujo Másico',
                'verbose_name_plural': 'Unidades Flujo Másico',
                'db_table': 'unidad_flujo_masico',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Potencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_potencia', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Unidad Potencia Caldera',
                'verbose_name_plural': 'Unidades de Potencia Caldera',
                'db_table': 'unidad_potencia',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Presion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_presion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Unidad de Presión Caldera',
                'verbose_name_plural': 'Unidades de Presión Caldera',
                'db_table': 'unidad_presion',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Simulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_simulacion', models.CharField(max_length=100, verbose_name='Nombre de simulación')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Simulaciones',
                'db_table': 'simulaciones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=400, verbose_name='Institución')),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceso', models.CharField(blank=True, max_length=100)),
                ('aplicaciones', models.ManyToManyField(to='formapp.aplicacion')),
            ],
            options={
                'verbose_name': 'Proceso Industrial',
                'verbose_name_plural': 'Procesos Industriales',
                'db_table': 'procesos',
            },
        ),
        migrations.CreateModel(
            name='FormSim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_simulacion', models.CharField(max_length=100, unique=True, verbose_name='Nombre de simulación')),
                ('demanda_anual', models.FloatField(max_length=300)),
                ('demanda_enero', models.FloatField(max_length=300)),
                ('demanda_febrero', models.FloatField(max_length=300)),
                ('demanda_marzo', models.FloatField(max_length=300)),
                ('demanda_abril', models.FloatField(max_length=300)),
                ('demanda_mayo', models.FloatField(max_length=300)),
                ('demanda_junio', models.FloatField(max_length=300)),
                ('demanda_julio', models.FloatField(max_length=300)),
                ('demanda_agosto', models.FloatField(max_length=300)),
                ('demanda_septiembre', models.FloatField(max_length=300)),
                ('demanda_octubre', models.FloatField(max_length=300)),
                ('demanda_noviembre', models.FloatField(max_length=300)),
                ('demanda_diciembre', models.FloatField(max_length=300)),
                ('demanda_lun', models.BooleanField(default=True, max_length=300)),
                ('demanda_mar', models.BooleanField(default=True, max_length=300)),
                ('demanda_mie', models.BooleanField(default=True, max_length=300)),
                ('demanda_jue', models.BooleanField(default=True, max_length=300)),
                ('demanda_vie', models.BooleanField(default=True, max_length=300)),
                ('demanda_sab', models.BooleanField(default=True, max_length=300)),
                ('demanda_dom', models.BooleanField(default=True, max_length=300)),
                ('potencia_caldera', models.FloatField(max_length=300, verbose_name='Potencia Nominal Caldera')),
                ('presion_caldera', models.FloatField(max_length=300, verbose_name='Presión de la Caldera')),
                ('eficiencia_caldera', models.FloatField(blank=True, null=True)),
                ('temperatura_red', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura de la red')),
                ('temperatura_retorno', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura retorno')),
                ('t_enero', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura enero')),
                ('t_febrero', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura febrero')),
                ('t_marzo', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura marzo')),
                ('t_abril', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura abril')),
                ('t_mayo', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura mayo')),
                ('t_junio', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura junio')),
                ('t_julio', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura julio')),
                ('t_agosto', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura agosto')),
                ('t_septiembre', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura septiembre')),
                ('t_octubre', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura octubre')),
                ('t_noviembre', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura noviembre')),
                ('t_diciembre', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura diciembre')),
                ('t_salida', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Temperatura de salida')),
                ('nombre_colector', models.CharField(blank=True, default='Colector 1', max_length=200, verbose_name='Nombre de colector')),
                ('area_apertura', models.FloatField()),
                ('eficiencia_optica', models.FloatField()),
                ('coef_per_lineales', models.FloatField()),
                ('coef_per_cuadraticas', models.FloatField()),
                ('iam_longitudinal', models.FloatField(blank=True, null=True, verbose_name='IAM longitudinal')),
                ('precio_colector', models.FloatField()),
                ('cantidad_bat', models.PositiveIntegerField()),
                ('col_bat', models.PositiveIntegerField()),
                ('total_colectores', models.PositiveIntegerField(blank=True, null=True)),
                ('sup_colectores', models.FloatField(blank=True, null=True)),
                ('inclinacion_col', models.FloatField()),
                ('azimut', models.FloatField()),
                ('flujo_masico', models.FloatField()),
                ('volumen', models.FloatField(max_length=100)),
                ('espesor_aislante', models.FloatField(blank=True, null=True)),
                ('efectividad', models.FloatField(default='0.8')),
                ('costo_combustible', models.PositiveIntegerField(default='100')),
                ('costo_tanque', models.PositiveIntegerField(null=True)),
                ('balance', models.PositiveIntegerField(null=True)),
                ('instalacion', models.PositiveIntegerField(null=True)),
                ('operacion', models.PositiveIntegerField(null=True)),
                ('impuesto', models.FloatField(null=True)),
                ('descuento', models.FloatField(null=True)),
                ('inflacion', models.IntegerField(null=True)),
                ('aplicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.aplicacion')),
                ('combustible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.combustible')),
                ('esquema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='esquema_int', to='formapp.esquema')),
                ('ini_jornada', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.inicio_jornada')),
                ('material_aislamiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.material_aislamiento')),
                ('material_almacenamiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.material_almacenamiento')),
                ('procesos', models.ManyToManyField(blank=True, to='formapp.procesos')),
                ('relacion_aspecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.relacion_aspecto')),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.sector')),
                ('tabla_colectores', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.tabla_colectores')),
                ('tipo_caldera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.tipo_caldera')),
                ('tipo_fluido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.tipo_fluido')),
                ('trno_jornada', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.termino_jornada')),
                ('ubicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.ubicacion')),
                ('unidad_costo_combustible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.unidad_costo_combustible')),
                ('unidad_demanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.unidad_demanda')),
                ('unidad_flujo_masico', models.ForeignKey(default='kg/s', null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.unidad_flujo_masico')),
                ('unidad_potencia', models.ForeignKey(default='kW', null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.unidad_potencia')),
                ('unidad_presion', models.ForeignKey(default='bar', null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.unidad_presion')),
            ],
            options={
                'verbose_name': 'simulacion',
                'verbose_name_plural': 'simulaciones',
                'db_table': 'FormSim',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formapp.sector'),
        ),
    ]
