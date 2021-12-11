from django.db import models

class Caso_Cerrado (models.Model):
    id = models.IntegerField(primary_key=True)
    cc_motivo_desaparicion = models.CharField(max_length=100)
    cc_fecha_aparicion =  models.DateField()
    cc_id_desaparecido =  models.ForeignKey(Desaparecido, related_name='casos_cerrados', on_delete=models.CASCADE)