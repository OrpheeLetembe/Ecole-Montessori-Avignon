from django.contrib import admin

from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter


class PracticalLifeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start')


class SensoryMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start')


class MathAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start')


class LangageAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start')


class LetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start')


admin.site.register(PracticalLife, PracticalLifeAdmin)
admin.site.register(SensoryMaterial, SensoryMaterialAdmin)
admin.site.register(Math, MathAdmin)
admin.site.register(Langage, LangageAdmin)
admin.site.register(Letter, LetterAdmin)
