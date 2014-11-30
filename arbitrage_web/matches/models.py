from django.db import models


class MegabetMatchOdds(models.Model):
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    match_date = models.DateTimeField()
    home_team_win_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_team_win_odd = models.FloatField()

    class Meta:
        unique_together = (('home_team', 'away_team', 'match_date'))