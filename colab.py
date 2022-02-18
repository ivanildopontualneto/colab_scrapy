import scrapy
from scrapy.shell import inspect_response
import json
import sys

class ColabSpyder(scrapy.Spider):
    name = "colab"

    def start_requests(self):
        i = 1
        state_id = 1
        sys.stdout = open('out.json', 'wt')
        while True:
            try:
                url = 'https://api.colab.re/event/'+str(i)
                yield scrapy.Request(url=url, callback=self.parse, headers={"x-colab-application-id": "072ddd80-8549-11e3-bfea-d99610cacfa2",
                                                                            "x-colab-rest-api-key": "20a4fcf5-9ddd-4337-8dc9-537bfe045f32",
                                                                            "x-colab-user-auth-ticket": "beab2ea0-83cf-11ea-b82b-61e450c67385"})
                i+=1
            except Exception as e:
                break
    
    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        print(jsonresponse)
        print(", ")
