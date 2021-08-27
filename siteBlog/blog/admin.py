from django.contrib import admin

from .models import Post, Autor
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "autor", "criado", "atualizado","status")
    prepopulated_fields = {"slug" : ("titulo",)}
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)