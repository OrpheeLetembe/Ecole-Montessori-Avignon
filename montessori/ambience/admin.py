from django.contrib import admin


from .models import Ambience


class AmbienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_start', 'date_end')


admin.site.register(Ambience, AmbienceAdmin)

