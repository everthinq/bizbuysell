import scrapy
import json
from datetime import datetime


class BizBuySellSpider(scrapy.Spider):
    name = "bizbuysell"
    allowed_domains = ["bizbuysell.com"]
    start_urls = ["https://www.bizbuysell.com/established-businesses-for-sale/1/"]

    def parse(self, response):
        yield scrapy.Request(
            method='POST',
            url='https://api.bizbuysell.com/bff/v2/BbsBfsSearchResults',
            headers={'content-type': 'application/json'},
            body=json.dumps({"bfsSearchCriteria": {"pageNumber": response.meta['depth'] + 1, "listingTypeIds": [40]}}),
            callback=self.parse_json)

        next_page = response.css("ul.ngx-pagination li.active + li > a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_json(self, response):
        json_data = json.loads(response.text)

        for item in json_data['value']['bfsSearchResult']['value']:
            if item['header']:
                yield {
                    "title": item.get('header') or None,
                    "description": item.get('description') or None,
                    'industry': json_data['value']['bfsSearchResult']['displayUrl'],  # there is no field like that in the api
                    'location': item['location'],
                    'asking_price': item['price'],
                    'revenue': None,  # there is no field like that in the api
                    'ebitda': item['ebitda'],
                    'cash_flow': item['cashFlow'],
                    'agent_name': item['contactInfo']['contactFullName'] if
                    item.get('contactInfo') and item['contactInfo'].get('contactFullName') else None,
                    'agent_company': item['contactInfo']['brokerCompany'] if
                    item.get('contactInfo') and item['contactInfo'].get('brokerCompany') else None,
                    'agent_phone': item['contactInfo']['contactPhoneNumber']['telephone'] if
                    item.get('contactInfo') and item['contactInfo'].get('contactPhoneNumber') else None,
                    'agent_tpnPhone': item['contactInfo']['contactPhoneNumber']['tpnPhone'] if
                    item.get('contactInfo') and item['contactInfo'].get('contactPhoneNumber') else None,
                    'website_url': item['urlStub'],
                    'created_at': datetime.now(),
                    'updated_at': datetime.now(),
                }
