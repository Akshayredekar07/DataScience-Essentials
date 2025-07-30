import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    author = scrapy.Field()
    
import re

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    def parse(self, response):
        # Extract book articles
        articles = response.css('article.product_pod')
        for article in articles:
            item = BookItem()
            try:
                # Extract title
                item['title'] = article.css('h3 a::attr(title)').get(default='').strip()
                
                # Extract price and clean it
                price_text = article.css('p.price_color::text').get(default='£0.00')
                item['price'] = float(re.sub(r'[^\d.]', '', price_text))
                
                # Extract rating
                rating_class = article.css('p.star-rating::attr(class)').get(default='')
                rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
                item['rating'] = rating_map.get(rating_class.split()[-1], 0)
                
                # Extract author (not directly available, use placeholder)
                item['author'] = article.css('p.author::text').get(default='Unknown').strip()
                
                yield item
            except Exception as e:
                self.logger.error(f"Error parsing book: {e}")
                continue
        
        # Follow pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            if not next_page.startswith('catalogue/'):
                next_page = 'catalogue/' + next_page
            yield response.follow(next_page, callback=self.parse)