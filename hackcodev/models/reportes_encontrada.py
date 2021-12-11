from django.db import models

class Reportes_Encontrada(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    p_notifica_cedula            = models.IntegerField(blank=False, null=False)
    p_notifica_nombres           = models.CharField(max_length = 50, blank=False, null=False)
    p_notifica_apellidos         = models.CharField(max_length = 50, blank=False, null=False)
    p_notifica_telefono          = models.IntegerField(blank=False, null=False)
    p_notifica_lugar_encontrado  = models.CharField(max_length = 100, blank=False, null=False)
    p_notifica_direccion         = models.CharField(max_length = 100, blank=False, null=False)
    p_notifica_tipo_sangre       = models.CharField(max_length = 50, blank=False, null=False)
    p_id_desaparecido_fk         = models.ForeignKey(Desaparecido, related_name='desaparecido_reportes_encontrada', on_delete=models.CASCADE)
    
    
    
    
    