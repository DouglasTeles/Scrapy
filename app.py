import scrapy


class testeSpider(scrapy.Spider):
    name = 'nome'
    start_urls = ['https://www.infomoney.com.br/ferramentas/cambio/']


    def parse(self, response):
        description = response.xpath("/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[5]/td[1]/text()").getall()
        for t in description:
            yield{
                'descricao':response.xpath("/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[5]/td[1]/text()").getall(),
                'valor':response.xpath("//*[@id='container_table']/table/tbody/tr[5]/td[3]/text()").getall()
            }


# # Mapeia site
# scrapy shell site

# # Pega texto: Dolar Comercial
# response.xpath("/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[5]/td[1]/text()").getall()

# # Pega valor Compra:
# response.xpath("//*[@id='container_table']/table/tbody/tr[5]/td[3]/text()").getall()


# # roda script
# scrapy runspider blah.py -o myjayson.json -s FEED_EXPORT_ENCODING=utf-8
