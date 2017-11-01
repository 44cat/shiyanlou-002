import scrapy

class Git_Name_Time(scrapy.Spider):
    
    name = 'shiyanlourepos-name-time'
    
    @property
    def strat_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}tab=repositories'
        
        return (url_tmpl.format(i) for i in range(1,5))
        
    def parse(self,response):
        for repos in response.css("li.py-4"):   
            yield {
                "name":repos.css("div.d-inline-block a::text()").re_first('\n\s*(.*)'),
                "update_time":repos.css("div.f6 relative-time::attr(datetime)").extract_first()
              }


#//*[@id="user-repositories-list"]/ul/li[1]/div[1]/h3/a*
#//*[@id="user-repositories-list"]/ul/li[1]/div[3]/relative-tilme

#"name":repos.xpath('./ul/li/div/h3//a[@itemprop="name codeRepository]/text()').re_first('\n\s*(.*)'),
#"update_time":repos.xpath('./ul/li//relative-time/@datetime').extract_first()

#repos.xpath('.//a[@itemprop="name codeRepository]/text()').re_first('\n\s*(.*)')
#repos.xpath('.//relative-time/@datetime').extract_first()


