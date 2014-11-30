from django.contrib import admin
from . import models
# Register your models here.
class MegabetMatchOddsAdmin(admin.ModelAdmin):
    list_display=('home_team', 'away_team', 'match_date', 'home_team_win_odd', 'draw_odd', 'away_team_win_odd')

admin.site.register(models.MegabetMatchOdds, MegabetMatchOddsAdmin)