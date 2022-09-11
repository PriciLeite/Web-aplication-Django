from django.contrib import admin
from rango.models import category, page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

#Personalizando a classe para preenchimento automatico do 'Slug' ao digitar a category.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} 

#Atualiza o registro incluindo 'categoryAdmin' para incluir a classe persolizada
admin.site.register(category, categoryAdmin)
admin.site.register(page, PageAdmin)
