from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import *

#from django.db import Sum



# Formulario para creación de usuarios

class UserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = 'on'
    
    first_name = forms.CharField(max_length=50)
    first_name.label = 'Nombre'
    last_name = forms.CharField(max_length=50)
    last_name.label = 'Apellido'
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)
    email.label = 'Correo ELectrónico'
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    institucion = forms.CharField(label='Institucion Eduacional o Empresa', max_length=200)
    
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','password1','password2','institucion')
        labels = {'username': _("Nombre de Usuario")}

# Actualización datos del usuario

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email']  
        
# Formulario de contacto

class ContactformForm(forms.Form):
    customer_email = forms.EmailField(label='Correo electrónico')
    customer_name = forms.CharField(max_length= 64,label='Nombre')
    subject = forms.CharField(max_length=255, label='Asunto')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = Contactform
        fields = ['customer_email', 'customer_name', 'subject', 'message']

# Formulario simulador

class FormSim(forms.ModelForm):
   
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(),widget=forms.Select(attrs={'class': 'browser-default'}))
    aplicacion = forms.ModelChoiceField(queryset= Aplicacion.objects.none(), to_field_name='aplicacion', widget=forms.Select(attrs={'class': 'browser-default'}), required=False)
    #aplicacion = forms.ModelChoiceField(queryset= Aplicacion.objects.none(), to_field_name='aplicacion', widget=forms.Select(attrs={'class': 'browser-default'}), required=False)
    #procesos = forms.ModelMultipleChoiceField(queryset=Procesos.objects.none(),  widget=forms.CheckboxSelectMultiple(), initial=False, required=False)
    procesos = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple,required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aplicacion'].queryset = Aplicacion.objects.none()
        #self.fields['proceso'].queryset = Procesos.objects.none()
        
        

    def aplicacion_choices(self):
        sector_id = self.data.get('sector')
        if sector_id:
            self.fields['aplicacion'].queryset = Aplicacion.objects.filter(sector_id=sector_id)
        
    def procesos_choices(self):
        aplicacion_id = self.data.get('aplicacion')
        if aplicacion_id:
            self.fields['procesos'].choices = [(p.id, p.proceso) for p in Procesos.objects.filter(aplicacion=aplicacion_id)]
    
    
    nombre_ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), to_field_name='nombre_ubicacion', widget=forms.Select(attrs={'class': 'form-select'}), initial="Santiago")
    latitud = forms.FloatField(widget=forms.NumberInput(attrs={'step': '0.01'}))
    longitud = forms.FloatField(widget=forms.NumberInput(attrs={'step': '0.01'}))
    combustible =forms.ModelChoiceField(queryset=Combustible.objects.all(), to_field_name='combustible', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label=" ", initial="Diesel")
    ini_jornada = forms.ModelChoiceField(queryset=Inicio_Jornada.objects.all(), to_field_name='ini_jornada', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label=" ", initial="00:00")
    term_jornada = forms.ModelChoiceField(queryset=Termino_Jornada.objects.all(), to_field_name='term_jornada', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label=" ", initial="23:30") 
    demanda_anual= forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}),required = False)
    unidad_demanda = forms.ModelChoiceField(queryset=Unidad_Demanda.objects.all(), to_field_name='unidad_demanda', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label=" Unidad de demanda", initial="l")
    unidad_potencia = forms.ModelChoiceField(queryset=Unidad_Potencia.objects.all(), to_field_name='unidad_potencia', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Unidad de Potencia", initial="kW")
    unidad_presion = forms.ModelChoiceField(queryset=Unidad_Presion.objects.all(), to_field_name='unidad_presion', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Unidad de Presión", initial="bar")
    sup_colectores = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}),required = False)
    total_colectores = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}),required = False)
    tipo_caldera = forms.ModelChoiceField(queryset=Tipo_Caldera.objects.all(), to_field_name='tipo_caldera', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Tipo de caldera")
    nombre_colector = forms.CharField(initial='TEST',required=False)
    unidad_flujo_masico = forms.ModelChoiceField(queryset=Unidad_Flujo_Masico.objects.all(), to_field_name='unidad_flujo_masico', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Unidad Flujo Másico", initial="kg/s")
    tipo_fluido = forms.ModelChoiceField(queryset=Tipo_Fluido.objects.all(), to_field_name='tipo_fluido', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Tipo de Fluido", initial="Glicol 10%")
    rango_flujo_prueba = forms.FloatField(required=False)
    iam = forms.FloatField()
    iam_longitudinal = forms.FloatField(required = False)
    relacion_aspecto = forms.ModelChoiceField(queryset=Relacion_Aspecto.objects.all(), to_field_name='relacion_aspecto', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Relación de Aspecto", initial="2")
    material_almacenamiento = forms.ModelChoiceField(queryset=Material_Almacenamiento.objects.all(), to_field_name='material_almacenamiento', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Material Almacenamiento", initial="Acero inoxidable")
    material_aislamiento = forms.ModelChoiceField(queryset=Material_Aislamiento.objects.all(), to_field_name='material_aislamiento', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Material Aislamiento", initial="Lana de vidrio")
    unidad_costo_combustible= forms.ModelChoiceField(queryset=Unidad_Costo_Combustible.objects.all(), to_field_name='unidad_costo_combustible', widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Unidad Costo Combustible", initial="$/l") 
    t_enero = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_febrero = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_marzo = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_abril = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_mayo = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_junio = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_julio = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_agosto = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_septiembre = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_octubre = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_noviembre = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    t_diciembre = forms.FloatField(widget=forms.NumberInput(attrs={'readonly':'readonly'}))
    siglas_esquema = forms.CharField(required=False,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    

        
    class Meta:
        model = FormSim
        fields = '__all__'
    
    
