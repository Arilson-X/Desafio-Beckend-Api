from re import search
from django.contrib import admin
from fornecedores.models import RegistroFornecedores

class Registros(admin.ModelAdmin):
    list_display = ('id','name','company','created_at','amount_products')
    list_display_link = ('id','name','company')
    search_fiels = ('id','name','company',)
    list_per_page = 16

admin.site.register(RegistroFornecedores,Registros)