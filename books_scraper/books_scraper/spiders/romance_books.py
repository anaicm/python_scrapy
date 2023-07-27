import scrapy


class RomanceBooksSpider(scrapy.Spider):
    name = "romance_books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

   
  
    def parse(self, response):
        categories = response.xpath("//div[@class='side_categories']/ul/li/ul/li/a")        
        for category in categories:
            category_name = category.xpath("./text()").get().strip()
            if category_name == "Romance":
                catalogo = category.xpath("./@href").get()
                category_url = response.urljoin(catalogo)
                yield scrapy.Request(url=category_url, callback=self.parse_books)
                
    def parse_books(self, response):
        books =  response.xpath("//article[@class='product_pod']")
        for book in books:
            title = book.xpath(".//h3/a/@title").get()
            price = book.xpath(".//p[@class='price_color']/text()").get()
            stock_element = book.xpath('.//p[contains(@class, "instock")]').get()
            image_url = book.xpath('.//img/@src').get()
            book_data = {
                'title': title,
                'price': float(price[1:]),
                'stock': "instock" in stock_element,
                'imageUrl': response.urljoin(image_url)
            }

            yield book_data
            
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_books)
