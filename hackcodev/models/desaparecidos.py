from django.db import models

class Desaparecido(models.Model):
    id = models.IntegerField(primary_key=True)
    des_cedula = models.DecimalField(max_length=20)
    des_nombre = models.CharField(max_length= 100)
    des_apellido = models.CharField(max_length= 100)
    des_edad = models.IntegerField(max_length= 100)
    des_fecha_desaparecido = models.DateField(auto_now=False, auto_now_add=False)
    des_foto = models.CharField(max_length= 1000)
    des_tipo_sangre = models.CharField(max_length= 5)
    des_sexo = models.CharField(max_length= 2)
    des_color_piel = models.CharField(max_length= 20)
    des_ciudad_recidencia = models.CharField( max_length= 50)
    des_estatura = models.FloatField(max_length= 20)
    des_estado_caso = models.BooleanField(default=True)
    
    fam_nombre = models.CharField(max_length= 100)
    fam_apellido = models.CharField(max_length= 100)
    fam_telefono = models.DecimalField(max_length= 20)
    fam_email = models.CharField(max_length= 100)
    




