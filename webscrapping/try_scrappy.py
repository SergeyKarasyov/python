import scrapy
from scrapy.crawler import CrawlerProcess

class PythonEventsSpider(scrapy.Spider):
    name = 'pythoneventsspider'

    start_urls = ['https://drewnowska43.pl/_get/budynek/1.2/etap/II/pietro/1/nr/m1.4',]
    found_events = []

    def parse(self, response):
        print(response.xpath('//div[contains(@class,"statisticFlat")]/div'))
        for event in response.xpath('//span[contains(@class, "priceMkwBrutto")]/li'):
            event_details = dict()
            event_details['name'] = event.xpath('h3[@class="event-title"]/a/text()').extract_first()
            event_details['location'] = event.xpath('p/span[@class="event-location"]/text()').extract_first()
            event_details['time'] = event.xpath('p/time/text()').extract_first()
            self.found_events.append(event_details)

if __name__ == "__main__":
    process = CrawlerProcess({ 'LOG_LEVEL': 'ERROR'})
    process.crawl(PythonEventsSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()
    print(spider)
    # for event in spider.found_events: print(event)