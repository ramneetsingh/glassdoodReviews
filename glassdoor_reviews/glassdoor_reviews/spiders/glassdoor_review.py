# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import Spider
from glassdoor_reviews.items import GlassdoorReviewsItem

class GlassdoorReviewSpider(Spider):
    name = 'glassdoor_review'
	
    allowed_domains = ['www.glassdoor.co.in']
    locations = ['india']
	
    country = {'india':'https://www.glassdoor.co.in/Reviews/india-reviews-SRCH_IL.0,5_IN115.htm' 
    }
	
    urls = []
	 
	
    for location in locations:
        urls.append(country[location])
    
    start_urls = urls
	
    '''rules = (
        Rule(LinkExtractor(allow=('-reviews-'),restrict_css=('.next',)),
            callback= 'parse_start_url',
            follow=True),
			
		Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
            callback= 'parse_review',
            follow=True)
			)'''

    def parse(self, response):
        #Extracting the content using css selectors
        reviews_link = []
        
        companies = response.xpath('//div[@class = "header cell info"]/div/a/text()').extract()
        rev_links = response.xpath('//div[@class = "empLinks tbl noswipe"]/a[@class="eiCell cell reviews"]/@href').extract();
        country = response.xpath('//div[@class = "condensed showHH"]/span/text()').extract();
            
       
        #Give the extracted content row wise
        for company , link in zip(companies , rev_links): 
            #print(country)			
            item = GlassdoorReviewsItem()
            item['country'] = country[0].split()[2];
            item['company'] = company;
            
            reviews_link = "https://www.glassdoor.co.in" + link
                
            yield Request(reviews_link, callback = self.parse_review , meta = {'item':item})
            
		
    def parse_review(self, response):
       
        item = response.meta['item']
        result = []
		
			
        #reviews = response.css('.summary::text').extract()
        reviews = response.xpath('//div[@class="cell"]/h2/a/span/text()').extract();
		
        #Give the extracted content row wise
        for review in reviews:
            review = review[1:-1]
            result.append(review);
                
        #next page
        next_page = response.xpath('//li[@class = "next"]/a/@href').extract()
        print(next_page)
		
        if next_page == '':
            item['review'] = result
            yield item
        else:
            next_page_link = "https://www.glassdoor.co.in" + next_page[0]
            print(next_page_link)
		
            yield Request(next_page_link, callback = self.parse_review ,meta = {'item':item})
		
        
			
       
	    
		
			
			
            
	    
            
			
	    
	    
        
