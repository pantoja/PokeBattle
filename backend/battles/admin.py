from django.contrib import admin

from battles.models import Battle, Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ("trainer", "battle")


admin.site.register(Battle)
admin.site.register(Team, TeamAdmin)
