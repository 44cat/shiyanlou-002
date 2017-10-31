import scrapy

class Git_Name_Time(scrapy.Spider):
    
    name = 'shiyanlourepos-name-time'
    
    @property
    def strat_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}tab=repositories'
        
        return (url_tmpl.format(i) for i in range(1,5))
        
    def parse(self,response):    
        #yield {
        print(response.css('div#user-repositories-list ul li div h3 a::text').re_first('\n        (.+)'))
        print(response.css('div#user-repositories-list ul li div relative-time::attr(datetime)').extract_first())

