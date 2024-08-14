import scrapy
from scrapy.http import FormRequest
from dotenv import dotenv_values
import scrapy

config = dotenv_values(".env") 
ICC_USER =config['ICC_USER']
ICC_PASSWORD = config['ICC_PASSWORD']

class StationSpider(scrapy.Spider):
    
    name = "stationspider"
    allowed_domains = ["redmet.icc.org.gt"]
    start_urls = ["https://redmet.icc.org.gt/redmet/comparativas"]
    


    def parse(self, response):
        input_hidden_token = response.xpath('//input[@type="hidden" and @name="_token"]').attrib['value']
        print(f"Hidden Token: {input_hidden_token}")
        return FormRequest.from_response(
            response,
            formdata={'_token': input_hidden_token,
                      'email': ICC_USER,
                      'password': ICC_PASSWORD},
            callback=self.after_login)
        
    
    def after_login(self, response):  
        
        pass