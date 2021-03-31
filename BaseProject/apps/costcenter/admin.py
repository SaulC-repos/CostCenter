from django.contrib import admin
from .models import Product, Coin, ExchangeCenter, Transaction, Wallet

# Register your models here.


class CurrencyAdminModel(admin.ModelAdmin):
    search_fields = ['name', "symbol"]  # Busqueda por tipo
    list_display = ["name", "abbreviation", "symbol"]  # Ver como tabla desde el admin


class ExchangeCenterAdminModel(admin.ModelAdmin):
    search_fields = ["rota_equivalence", 'coin__symbol']
    list_display = ["coin_value", "rota_equivalence", "coin"]


admin.site.register(Coin, CurrencyAdminModel)
admin.site.register(ExchangeCenter, ExchangeCenterAdminModel)
admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(Product)
