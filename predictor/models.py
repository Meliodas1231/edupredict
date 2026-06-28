from django.db import models


class GuiaReparto(models.Model):
    """Reparto de diapositivas y bloques de la guía de presentación (equipo)."""

    clave = models.CharField(max_length=64, unique=True, default='equipo')
    slides = models.JSONField(default=dict, blank=True)
    partes = models.JSONField(default=dict, blank=True)
    modificado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reparto guía presentación'
        verbose_name_plural = 'Repartos guía presentación'

    def __str__(self):
        return f'Guía · {self.clave}'
