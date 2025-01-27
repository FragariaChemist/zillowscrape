import scrapy
import json


class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    allowed_domains = ["zillow.com"]
    url = "https://www.zillow.com/los-angeles-ca/"
    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)
    
    def parse(self, response):

        next_data_script = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()

        data = json.loads(next_data_script)

        homes = data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']
        
        for home in homes:

            home_data = {
                'home_type': home['hdpData']['homeInfo'].get('homeType', None),
                'days_posted': str(home['hdpData']['homeInfo'].get('daysOnZillow', None)),
                'home_URL': home.get('detailUrl', None),
                'home_main_image': home.get('imgSrc', None),
                'home_status': home.get('statusType', None),
                'home_price': home.get('price', None),
                'home_address': home.get('address', None),
                'home_zipcode': home.get('addressZipcode', None),
                'num_beds': home.get('beds', None),
                'num_baths': home.get('beds', None),
                'home_area': home.get('area', None)
            }
            yield home_data

        next_page_url = data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination'].get('nextUrl', None)

        if (next_page_url):
            next_page_full_url = 'https://www.zillow.com/' + data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination'].get('nextUrl', None)
            print(next_page_url)
            yield scrapy.Request(url=next_page_full_url, callback = self.parse)