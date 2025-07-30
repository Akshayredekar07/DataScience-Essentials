BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    'bookscraper.pipelines.BookscraperPipeline': 300,
}

# Limit depth for this example (approx. 3 pages)
DEPTH_LIMIT = 3