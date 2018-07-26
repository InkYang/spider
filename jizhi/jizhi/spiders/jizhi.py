import scrapy
import sys

class Jizhi(scrapy.Spider):

    name = 'jizhi'

    arg = ' '.join(sys.argv[3:])

    base_urls = "http://www.baidu.com"

    start_urls = [
        'http://www.baidu.com/s?{}'.format(arg)
    ]

    counter = 0

    def parse(self, response):

        result_lst = response.css("h3.t a::text")

        for result in result_lst:
            yield {
                'title':result.extract()
            }

        Jizhi.counter +=1

        # next_page:css('a.n')

        if Jizhi.counter == 5: return        

        next_page = response.css('a.n::attr(href)')

        if len(next_page) == 2:
            next_page_url = next_page[1].extract()
        else:
            next_page_url = next_page.extract_first()

        yield scrapy.Request(self.base_urls + next_page_url, callback=self.parse)