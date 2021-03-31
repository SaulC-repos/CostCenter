from django.contrib.auth.models import AbstractUser
from django.db import models
from stdimage import StdImageField
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{8,14}((,\d{8,14})?)*$',
                             message="El formato del teléfono debe ser: '9998888777', "
                                     "sin código de país. De 8-14 dígitos permitidos. "
                                     "Puede agregar más telefonos seperados por coma.")


class User(AbstractUser):
    TYPE = (
        ('Admin', 'Administrador'),
        ('Tec', 'Técnico'),
        ('Ventas', 'Ventas')
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')
    avatar = StdImageField(upload_to='usuarios/%Y/%m/',
                           variations={'perfil': {"width": 240, "height": 240, "crop": True},
                                       'thumbnail': {"width": 45, "height": 45, "crop": True}},
                           default="usuarios/avatar.png")
    direccion = models.TextField(blank=True)
    telefono = models.CharField(validators=[phone_regex], max_length=250, blank=True, verbose_name="Teléfono Celular")

    def __str__(self):
        return '{}'.format(self.username)


class Address(models.Model):
    """
    This model represents address for international
    requirements
    """

    street_address = models.CharField(
        verbose_name="Indica una dirección postal precisa",
        max_length=200
        )
    route = models.CharField(
        verbose_name="Indica una ruta con nombre",
        max_length=150, blank=True, null=True
        )
    point_of_interest = models.CharField(
        verbose_name="Indica un punto de interés con nombre",
        max_length=150, blank=True, null=True
        )
    park = models.CharField(
        verbose_name="Parque cercano",
        max_length=150, blank=True, null=True
        )
    airport = models.CharField(
        verbose_name="Aeropuerto cercano",
        max_length=150, blank=True, null=True
        )
    natural_feature = models.CharField(
        verbose_name="indica una característica natural prominente",
        max_length=150, blank=True, null=True
        )
    postal_code = models.CharField(
        verbose_name="Código postal",
        max_length=150, blank=True, null=True
        )
    plus_code = models.CharField(
        verbose_name="Referencia de ubicación codificada(Plus code)",
        max_length=150, blank=True, null=True
        )
    neighborhood = models.CharField(
        verbose_name="Vecindario",
        max_length=150, blank=True, null=True
        )
    locality = models.CharField(
        verbose_name="Localidad",
        max_length=150, blank=True, null=True
        )
    sublocality = models.CharField(
        verbose_name="Entidad civil de primer orden debajo de una localidad",
        max_length=150, blank=True, null=True
        )
    colloquial_area = models.CharField(
        verbose_name="Nombre de uso común para la entidad",
        max_length=150, blank=True, null=True
        )
    administrative_area_level_1 = models.CharField(
        verbose_name="Entidad civil por debajo del nivel de país",
        max_length=150, blank=True, null=True
        )
    administrative_area_level_2 = models.CharField(
        verbose_name="Entidad civil por debajo del nivel de país",
        max_length=150, blank=True, null=True
        )
    country = models.CharField(
        verbose_name="Indica la entidad política nacional",
        max_length=150, blank=True, null=True
        )
    political = models.CharField(
        verbose_name="entidad política",
        max_length=150, blank=True, null=True
        )
    is_fiscal = models.BooleanField(
        verbose_name="¿Es una dirección fiscal?",
        default=False
        )

    class Meta:
        verbose_name = ("Dirección")
        verbose_name_plural = ("Dirección")

    def __str__(self):
        return self.street_address
