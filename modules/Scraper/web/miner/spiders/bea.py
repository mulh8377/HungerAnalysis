import scrapy

class BEASpider(scrapy.Spider):
    name = "bea"

    def start_requests(self):
        urls = ["https://www.bea.gov/",
                "https://www.bea.gov/data/gdp",
                "https://www.bea.gov/data/by-place-us",
                "https://www.bea.gov/data/economic-accounts"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(selfself, response):
        print(response)