import scrapy
import requests
import unittest
url = 'https://brickset.com/sets/year-2006'
h = requests.head(url)
print("Header:")
print("**********")
r = requests.get('https://brickset.com/sets/year-2006')
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {'User-Agent' : 'Mobile'}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
print("Status code:")
print("\t *", h.status_code)
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(h.status_code, 200)
if __name__ == '__main__':
    unittest.main()
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2006']

    def parse(self, response):
        css_selector = 'img'

        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )