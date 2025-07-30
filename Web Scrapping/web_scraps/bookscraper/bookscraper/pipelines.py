import pandas as pd

class BookscraperPipeline:
    def __init__(self):
        self.books = []
    
    def process_item(self, item, spider):
        # Clean data
        item['title'] = item['title'].strip() if item['title'] else 'Unknown'
        item['author'] = item['author'].strip() if item['author'] else 'Unknown'
        item['price'] = round(float(item['price']), 2) if item['price'] else 0.0
        item['rating'] = int(item['rating']) if item['rating'] else 0
        self.books.append(item)
        return item
    
    def close_spider(self, spider):
        # Create DataFrame and export to CSV
        df = pd.DataFrame(self.books, columns=['title', 'author', 'price', 'rating'])
        try:
            df.to_csv('books_data.csv', index=False, encoding='utf-8')
            spider.logger.info(f"Data exported to 'books_data.csv'. Total books: {len(df)}")
        except Exception as e:
            spider.logger.error(f"Failed to export data: {e}")