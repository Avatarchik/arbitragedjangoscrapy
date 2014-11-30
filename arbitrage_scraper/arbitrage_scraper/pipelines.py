from django.db import IntegrityError

from .items import MegabetMatchOddsItem

import django
django.setup()

class MegabetScraperPipeline(object):
    def process_item(self, item, spider):

        try:
            item.save()
        except IntegrityError:
            item = MegabetMatchOddsItem.django_model.objects.filter(
                home_team=item['home_team'],
                away_team=item['away_team'],
                match_date=item['match_date']
                ).update(
                    home_team_win_odd=item['home_team_win_odd'],
                    draw_odd=item['draw_odd'],
                    away_team_win_odd=item['away_team_win_odd']
                )

        return item
        """print "{}\n{}\n{}\n{}\n{}\n{}\n".format(
                        item['home_team'],
                        item['away_team'],
                        item['match_date'],
                        item['home_team_win_odd'],
                        item['draw_odd'],
                        item['away_team_win_odd']
                    )"""
