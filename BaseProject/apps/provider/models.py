from django.db import models

# Create your models here.

class ProviderType(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=30, unique=True)
    is_active = models.BooleanField(verbose_name="¿Está activo?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Tipo de proveedor"
        verbose_name_plural="Tipos de proveedores"


class Provider(models.Model):
