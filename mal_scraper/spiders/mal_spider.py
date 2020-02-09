import scrapy

class MALSpider(scrapy.Spider):
    name = 'mal'

    start_urls = ['https://myanimelist.net/topanime.php']

    def parse(self, response):
        # follow links to author pages
        for href in response.xpath("//a[@class='hoverinfo_trigger fl-l fs14 fw-b']/@href").getall()  :
            yield response.follow(href, self.parse_anime)

        # follow pagination links
        for href in response.xpath("//a[@class='link-blue-box next']/@href").getall():
            yield response.follow(href, self.parse)

    def parse_anime(self, response):

        yield {
            'name': response.xpath("//span[@itemprop='name']/text()").get(),
            'genre': response.xpath("//span[@itemprop='genre']/text()").getall(),
            'ratingValue': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'studios': response.xpath("//span/text()[contains(.,'Studios:')]/ancestor::node()[2]/a/text()").getall(),
            'episodes': response.xpath("//span/text()[contains(.,'Episodes:')]/following::text()").get().replace('\n', '').replace(' ', ''),
        }