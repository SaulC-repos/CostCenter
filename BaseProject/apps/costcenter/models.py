from django.db import models
from BaseProject.apps.custom_user.models import User


class Product(models.Model):
    """
    This model is the representation of a
    product included in a ticket
    """

    PRODUCT_TYPE = [
        ("Experiencia", "experience"),
        ("Tour", "tour"),
        ("Ticket", "ticket"),
        ("Extras", "extra"),
        ("Descuento", "discount"),
    ]

    name = models.CharField(
        verbose_name="Nombre",
        max_length=150, blank=True, null=True
    )
    product_type = models.CharField(
        verbose_name="Tipo de producto",
        max_length=50, choices=PRODUCT_TYPE
    )
    product_id = models.IntegerField(
        verbose_name="ID del producto"
    )

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("")

    def __str__(self):
        return self.name


class Coin(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=20, blank=True, null=True)
    abbreviation = models.CharField(verbose_name="Abreviación", max_length=5)
    symbol = models.CharField(verbose_name="Simbolo", max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"


class ExchangeCenter(models.Model):
    coin_value = models.DecimalField(
        verbose_name='Valor de la moneda',
        max_digits=20, decimal_places=2
    )
    rota_equivalence = models.DecimalField(
        verbose_name='Equivalencia Rotapuntos',
        max_digits=20, decimal_places=2
    )
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return self.coin.name

    class Meta:
        verbose_name = "Centro de Cambio"
        verbose_name_plural = "Centros de cambio"


class Wallet(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Usuario",
        on_delete=models.CASCADE
        )
    amount_wallet = models.DecimalField(
        verbose_name="Monto Wallet",
        max_digits=150, decimal_places=2
        )

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Monedero "
        verbose_name_plural = "Monederos"


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("Debit", "Debit"),  # Cargo
        ("Credit", "Credit")  # Abono
    )

    wallet = models.ForeignKey(Wallet, verbose_name="Monedero", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        verbose_name="Tipo de movimiento",
        max_length=150, default="", choices=TRANSACTION_TYPE
    )
    concept = models.CharField(verbose_name="Concepto", max_length=300, blank=True, null=True)
    reference = models.CharField(verbose_name="Referencia", max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.DecimalField(
        verbose_name="Monto de transaccion",
        max_digits=20, decimal_places=2
    )

    def __str__(self):
        return self.transaction_type

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
