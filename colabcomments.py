import scrapy
import json
#from pprint import pprint

class ColabcommentsSpider(scrapy.Spider):
    name = 'colabcomments'

    def start_requests(self):
        with open('r"C:\Users\ivani\Desktop\Json\Niteroi.json"') as f:
            data = json.loads(f)
            for event in data:
                if 'event' in event["share_url"]:
                    id = event["share_url"].replace(
                        'https://www.colab.re/event/', '')
                    url = event["share_url"].replace(
                        'www', 'api') + '/comments'
                        yield scrapy.Request(url=url, callback=self.parse, meta={'id': id}, headers={"x-colab-application-id": "072ddd80-8549-11e3-bfea-d99610cacfa2",
                                                                            "x-colab-rest-api-key": "20a4fcf5-9ddd-4337-8dc9-537bfe045f32",
                                                                            "x-colab-user-auth-ticket": "beab2ea0-83cf-11ea-b82b-61e450c67385"})

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for entry in jsonresponse:
            entry[event_id] = response.meta['id']
            yield entry    