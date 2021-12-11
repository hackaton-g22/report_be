from django.db      import models
from .desaparecidos import Desaparecido

class Caso_Cerrado (models.Model):
    id = models.IntegerField(primary_key=True)
    cc_motivo_desaparicion = models.CharField(max_length=100)
    cc_fecha_aparicion     =  models.DateField()
    desaparecido_fk        =  models.ForeignKey(Desaparecido, related_name='caso_cerrado', on_delete=models.CASCADE)