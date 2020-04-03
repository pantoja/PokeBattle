from django.contrib import admin

from battles.models import Battle, Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ("trainer", "battle")


class BattleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user_creator", "user_opponent")


admin.site.register(Battle, BattleAdmin)
admin.site.register(Team, TeamAdmin)
