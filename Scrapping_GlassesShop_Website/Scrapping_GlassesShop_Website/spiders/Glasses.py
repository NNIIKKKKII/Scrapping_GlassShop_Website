import scrapy


class GlassesSpider(scrapy.Spider):
    name = "Glasses"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        for product in response.xpath("//div[@class = 'product-list']/div[@class = 'pro_box']"):
            yield {
                "Product_Name" : product.xpath(".//div/div[2]/div/div/span[1]/text()").get(),
                "Product_Price": product.xpath(".//div/div[2]/div//div/span[2]/span/text()").get(),
                "Product_img_link" : response.urljoin(product.xpath(".//div/div/div/a[1]/@href").get()),
            }


        # next_page = response.xpath("//button[@class = 'btn-next is-last']/span")

        # if next_page:
        #     # next_page_url = response.urljoin(next_page.xpath("@href").get())
        #     yield scrapy.Request(url = next_page, callback = self.parse)

