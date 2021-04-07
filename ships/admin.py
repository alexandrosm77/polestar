from django.contrib import admin

from .models import Position, Ship

admin.site.register(Ship, admin.ModelAdmin)
admin.site.register(Position, admin.ModelAdmin)
