from rest_framework                         import serializers
from hackcodev.models.reportes_encontrada   import Reportes_Encontrada
from hackcodev.models.desaparecidos         import Desaparecido
class Reportes_Encontrada_Serializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Reportes_Encontrada
        fields = ['id', 'p_notifica_cedula', 'p_notifica_nombres', 'p_notifica_apellidos', 'p_notifica_telefono', 
                  'p_notifica_lugar_encontrado', 'p_notifica_direccion', 'p_notifica_tipo_sangre', 'p_id_desaparecido_fk']
        
    """def create(self, validated_data):
        print("Esta es la data que llega en el metodo created", validated_data)
        reporte_instance = Reportes_Encontrada.objects.create(**validated_data)
        return reporte_instance"""
    
    def to_representation(self, obj):  # de objeto a json
        reporte = Reportes_Encontrada.objects.get(id=obj.id)
        desaparecidos = Desaparecido.objects.get(id=obj.p_id_desaparecido_fk.id)
        
        return {
            "id": reporte.id,
            "p_notifica_cedula" : reporte.p_notifica_cedula,
            "p_notifica_nombres" : reporte.p_notifica_nombres,
            "p_notifica_apellidos" : reporte.p_notifica_apellidos,
            "p_notifica_telefono" : reporte.p_notifica_telefono,
            "p_notifica_lugar_encontrado" : reporte.p_notifica_lugar_encontrado,
            "p_notifica_direccion" : reporte.p_notifica_direccion,
            "p_notifica_tipo_sangre" : reporte.p_notifica_tipo_sangre,
            "desaparecido_fk" : {
                
                'id' : desaparecidos.id,
                'des_cedula' : desaparecidos.des_cedula,
                'des_nombre' :  desaparecidos.des_nombre,
                'des_apellido' : desaparecidos.des_apellido,
                'des_edad' : desaparecidos.des_edad,
                'des_fecha_desaparecido' : desaparecidos.des_fecha_desaparecido,
                'des_foto' : desaparecidos.des_foto,
                'des_tipo_sangre' : desaparecidos.des_tipo_sangre,
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
          
    }
        
        