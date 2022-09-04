from django.contrib import admin

from .models import Students


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'ambience')


admin.site.register(Students, StudentAdmin)


