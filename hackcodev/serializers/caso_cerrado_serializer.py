from rest_framework                      import serializers
from hackcodev.models.caso_cerrado_model import Caso_Cerrado
from hackcodev.models.desaparecidos         import Desaparecido

class Caso_Cerrado_Serializer(serializers.ModelSerializer): 
    class Meta: 
        model = Caso_Cerrado 
        fields = ['motivo_desaparicion', 'fecha_aparicion', 'desaparecido_fk']


def to_representation(self, obj):  # de objeto a json
        caso = Caso_Cerrado.objects.get(id=obj.id)
        desaparecido = Desaparecido.objects.get(id=obj.desaparecido_fk.id)
        
        return {
            "id": caso.id,
            "cc_motivo_desaparicion" : caso.cc_motivo_desaparicion,
            "cc_fecha_aparicion" : caso.cc_fecha_aparicion,
            "desaparecido_fk" : {
                'id'                    : desaparecido.id,
                'des_cedula'            : desaparecido.des_cedula,
                'des_nombre'            : desaparecido.des_nombre,
                'des_apellido'          : desaparecido.des_apellido,
                'des_edad'              : desaparecido.des_edad,
                'des_fecha_desaparecido': desaparecido.des_fecha_desaparecido,
                'des_foto'              : desaparecido.des_foto,
                'des_tipo_sangre'       : desaparecido.des_tipo_sangre,
                'des_sexo'              : desaparecido.des_sexo,
                'des_color_piel'        : desaparecido.des_color_piel,
                'des_ciudad_recidencia' : desaparecido.des_ciudad_recidencia,
                'des_estatura'          : desaparecido.des_estatura,
                'des_estado_caso'       : desaparecido.des_estado_caso,
                'fam_nombre'            : desaparecido.fam_nombre,
                'fam_apellido'          : desaparecido.fam_apellido,
                'fam_telefono'          : desaparecido.fam_telefono,
                'fam_email'             : desaparecido.fam_email
            }
          
    }