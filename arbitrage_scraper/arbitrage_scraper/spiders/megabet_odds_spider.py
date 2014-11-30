from datetime import datetime
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from arbitrage_scraper.items import MegabetMatchOddsItem


class MegabetOddsSpider(Spider):
    name = "megabet_odds"
    allowed_domains = ["megabetkz.com"]
    start_urls = [
        'http://megabetkz.com/Sport.aspx?sid=5',
    ]

    megabet_dict = {}
    def parse(self, response):
        selector = Selector(response)
        tables = selector.xpath('//table')
        for table in tables:
            table_rows = table.xpath('.//tr')

            for table_row in table_rows:
                raw_match_name = table_row.xpath('.//td[@class="it1 wt152"]/strong/text()').extract()
                raw_match_date = table_row.xpath('.//td[@class="it1 wt152"]/span/text()').extract()
                raw_match_odd1 = table_row.xpath('.//td[@class="it2 wt25 hoverable"][1]/em/text()').extract()
                raw_match_odd2 = table_row.xpath('.//td[@class="it2 wt25 hoverable"][2]/em/text()').extract()
                raw_match_odd3 = table_row.xpath('.//td[@class="it2 wt25 hoverable"][3]/em/text()').extract()

                if len(raw_match_name)!=0 and len(raw_match_date)!=0 and len(raw_match_odd1)!=0 and len(raw_match_odd2)!=0 and len(raw_match_odd3)!=0:
                    match_home = raw_match_name[0].strip(u' \xa0').encode('ascii', 'replace').split(' - ')
                    home_team = match_home[0]
                    away_team = match_home[1]
                    match_date = datetime.strptime(raw_match_date[0], '%d %B %Y, %H:%M')
                    match_odd1 = float(raw_match_odd1[0])
                    match_odd2 = float(raw_match_odd2[0])
                    match_odd3 = float(raw_match_odd3[0])

                    megabet_item = MegabetMatchOddsItem(
                        home_team=home_team,
                        away_team=away_team,
                        match_date=match_date,
                        home_team_win_odd=match_odd1,
                        draw_odd=match_odd2,
                        away_team_win_odd=match_odd3
                    )
                    
                    yield megabet_item

                    """item = {
                        'home_team': home_team,
                        'away_team': away_team,
                        'match_date': match_date,
                        'home_team_win_odd': match_odd1,
                        'draw_odd': match_odd2,
                        'away_team_win_odd': match_odd3
                    }
                    megabet_item.save()
                    megabet_dict[raw_match_name] = {'match_date': ''}
                    print "{}\n{}\n{}\n{}\n{}\n{}\n".format(
                        home_team,
                        away_team,
                        match_date,
                        match_odd1,
                        match_odd2,
                        match_odd3
                    )"""