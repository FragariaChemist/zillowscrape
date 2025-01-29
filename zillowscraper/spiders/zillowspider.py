import scrapy
import json
import csv


class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    allowed_domains = ["zillow.com"]
    url = "https://www.zillow.com/homes/Stevensville,-MD_rb/"

    custom_settings = {
        'FEEDS': {
            'home_details.csv': {'format':'csv',
                                'fields': ['home_type',
                                            'days_posted',
                                            'home_URL',
                                            'home_main_image',
                                            'home_status',
                                            'home_price',
                                            'home_address',
                                            'home_zipcode',
                                            'num_beds',
                                            'num_baths',
                                            'home_area'
                                            ]},
            'price_history.csv': {'format':'csv',
                                'fields': ['home_URL',
                                            'date',
                                            'price',
                                            'price_change_rate',
                                            'event']
                                            }
                                }
                }

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

            # Follow home URL to scrape price history
            home_url = home_data['home_URL']
            if home_url:
                yield scrapy.Request(
                    url = home_url,
                    callback = self.parse_home,
                    meta = {'home_URL': home_url}
                )

        next_page_url = data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination'].get('nextUrl', None)

        if (next_page_url):
            next_page_full_url = 'https://www.zillow.com/' + data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination'].get('nextUrl', None)
            print(next_page_url)
            yield scrapy.Request(url=next_page_full_url, callback = self.parse)

    def parse_home(self, response):
        next_data_script = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()

        try:
            data = json.loads(next_data_script)
            gdp_client_cache = data['props']['pageProps']['componentProps']['gdpClientCache']
            parsed_cache = json.loads(gdp_client_cache)
        except (KeyError, json.JSONDecodeError):
            return
        
        dynamic_key = next((key for key in parsed_cache.keys() if 'ViewShowcaseQuery' in key), None)
        if not dynamic_key:
            print(f'No dynamic key for URL: {response.url}')
            return
        
        price_history = parsed_cache.get(dynamic_key, {}).get('property', {}).get('priceHistory', [])
        if not price_history:
            print(f'No price history available for  URL: {response.url}')
            return
        
        for entry in price_history:
            date = entry.get('date')
            price = entry.get('price')
            price_change_rate =  entry.get('priceChangeRate')
            event = entry.get('event')

            if all([date, price, price_change_rate, event]):
                yield {
                    'home_URL':response.meta['home_URL'],
                    'date':date,
                    'price_change_rate':price_change_rate,
                    'event':event
                }
            else:
                print(f'No price history data for URL: {response.meta["home_URL"]}')