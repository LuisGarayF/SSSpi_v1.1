from rest_framework import serializers
from .models import FormSim

class FormSimSerializer(serializers.Serializer):
    class Meta:
        model = FormSim
        fields = ('id', 'nombre_simulacion', 'sector', 'aplicacion','procesos', 'ubicacion','esquema', 'combustible', 'ini_jornada', 'trno_jornada', 'demanda_anual','unidad_demanda','tabla_colectores',
                  'demanda_enero', 'demanda_febrero', 'demanda_marzo','demanda_abril','demanda_mayo','demanda_junio','demanda_julio','demanda_agosto','demanda_septiembre','demanda_octubre','demanda_noviembre'
                  'demanda_diciembre','demanda_lun','demanda_mar','demanda_mie','demanda_jue','demanda_vie','demanda_sab','demanda_dom','potencia_caldera','unidad_potencia','presion_caldera','unidad_presion'
                  'tipo_caldera','eficiencia_caldera','temperatura_red','temperatura_retorno','t_enero','t_febrero','t_marzo','t_abril','t_mayo','t_junio','t_julio','t_agosto','t_septiembre','t_octubre','t_noviembre',
                  't_diciembre','t_salida','area_apertura','eficiencia_optica','coef_per_lineales','coef_per_cuadraticas','iam_longitudinal','precio_colector','cantidad_bat','col_bat','total_colectores','sup_colectores',
                  'inclinacion_col','azimut','flujo_masico','tipo_fluido','volumen','relacion_aspecto','material_almacenamiento','material_aislamiento','espesor_aislante','efectividad','costo_combustible','unidad_costo_combustible'
                  'costo_tanque','balance','instalacion','operacion','impuesto','descuento','inflacion')
