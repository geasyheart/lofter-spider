# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""
import logging

from scrapy import Spider, Request

from lofter.items import LofterItem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("lofter")


class LofterArticleSpider(Spider):
    name = "lofter"

    start_urls = [
        "http://0x180.lofter.com/?page=1"
    ]

    def parse(self, response):
        # 获取下一页
        per_next_url = response.xpath("/html/body/div/div[2]/div/ul/li/div[2]/a/@href").extract()
        if len(per_next_url) == 2:
            next_page = per_next_url[-1]
        elif len(per_next_url) == 1:
            # 第2页
            find = per_next_url[0].find("page=2")
            if find == 1:
                next_page = per_next_url[0]
            else:
                next_page = None
        else:
            next_page = None
        if next_page:
            next_url = response.urljoin(next_page)
            logger.info("下一页的链接地址:{}".format(next_url))
            yield Request(next_url, callback=self.parse)

        # 获取文章title url
        title_urls = response.xpath("//div[@class='postinner']/div/div/h2/a/@href").extract()
        for title_url in title_urls:
            logger.info("当前访问的文章地址:{}".format(title_url))
            yield Request(title_url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.xpath("/html/body/div/div[2]/div/div/div[1]/div/div[1]/div/h2/a/text()").extract_first()
        # content = "".join(response.xpath("//div[@class='txtcont']/*").extract())
        x = response.xpath("//div[@class='txtcont']")
        content = x.xpath('string(.)').extract()[0]
        lofter_item = LofterItem()
        lofter_item['title'] = title
        lofter_item['content'] = content
        yield lofter_item
