from items import IceteaItem
import scrapy
from scrapy.loader import ItemLoader
class DrinkteaSpider(scrapy.Spider):
    name = 'drinkTea'
    allowed_domains = ['https://www.woolworths.com.au/']
    start_urls = ['http://https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas/']

    def parse(self, response):
        for bottle in response.css('a.shelfProductTile-information'):
            loader=ItemLoader(item=IceteaItem(), selector=bottle )
            loader.add_css('name','a.shelfProductTile-descriptionLink')
            loader.add_css('breadcrumbs','li.breadcrumbs-link ng-start-insreted span')
            yield loader.load_item()
