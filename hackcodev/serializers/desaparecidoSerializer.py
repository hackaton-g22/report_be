from django.db.models import fields
from rest_framework import serializers
from hackcodev.models.desaparecidos import Desaparecido
class DesaparecidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desaparecido
        fields = ['id', 'des_cedula', 'des_nombre', 'des_apellido', 'des_edad', 'des_fecha_desaparecido', 'des_foto', 'des_tipo_sangre', 'des_sexo', 'des_color_piel', 'des_ciudad_recidencia', 'des_estatura', 'des_estado_caso', 'fam_nombre', 'fam_apellido', 'fam_telefono','fam_email' ]
    
    def create(self, validated_data):
        desaparecidosInstance = Desaparecido.objects.create(**validated_data)
        return desaparecidosInstance
    
    def to_representation(self, obj):
        desaparecidos = Desaparecido.objects.get(id = obj.id)
        
        return {
            'id' : desaparecidos.id,
            'des_cedula' : desaparecidos.des_cedula,
            'des_nombre' :  desaparecidos.des_nombre,
            'des_apellido' : desaparecidos.des_apellido,
            'des_edad' : desaparecidos.des_edad,
            'des_fecha_desaparecido' : desaparecidos.des_fecha_desaparecido,
            'des_foto' : desaparecidos.des_foto,
            'des_tipo_sangre' : desaparecidos.des_tipp_sangre,
            'des_sexo' : desaparecidos.des_sexo,
            'des_color_piel' : desaparecidos.des_color_piel,
            'des_ciudad_recidencia' : desaparecidos.des_ciudad_recidencia,
            'des_estatura' : desaparecidos.des_estatura,
            'des_estado_caso' : desaparecidos.des_estado_caso,
            'fam_nombre' : desaparecidos.fam_nombre,
            'fam_apellido' : desaparecidos.fam_apellido,
            'fam_telefono' : desaparecidos.fam_telefono,
            'fam_email' : desaparecidos.fam_email,
        }
