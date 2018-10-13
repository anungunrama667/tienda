from django.contrib import admin
from Tienda.Apps.GestionCupones.model import*

# Register your models here.
admin.site.Register(Cliente)
admin.site.Register(Cupon)
admin.site.Register(AsignacionCupones)