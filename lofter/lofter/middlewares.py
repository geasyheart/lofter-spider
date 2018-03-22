# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals

from lofter.settings import USER_AGENTS


class LofterSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LofterDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentMiddleWare(object):
    def process_request(self, request, spider):
        """

        :param request:
        :param spider:
        :return:
        """
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-agent', useragent)
        return


# class ProxyMiddleware(object):
#     """
#     关于proxy, 可以安装scrapy-proxies,但是需要考虑网速
#     """
#
#     def __init__(self):
#         self.proxies = copy.copy(PROXY)  # type: dict
#
#     def process_request(self, request, spider):
#         """
#
#         :param request:
#         :param spider:
#         :return:
#         """
#         proxy_addr = random.choice(list(self.proxies.keys()))
#         request.meta['proxy'] = proxy_addr
#         proxy_pwd = self.proxies.get(proxy_addr)
#         if proxy_pwd:
#             b64 = base64.b64encode(self.proxies.get(proxy_addr).encode()).decode()
#             request.headers['Proxy-Authorization'] = 'Basic ' + b64
#
#     def process_exception(self, request, exception, spider):
#         """
#
#         :param request:
#         :param exception:
#         :param spider:
#         :return:
#         """
#         if 'proxy' not in request.meta:
#             return
#         proxy_addr = request.meta['proxy']
#         us = urlsplit(proxy_addr)
#         proxy_addr_netloc = us.netloc
#         try:
#             self.proxies.pop(proxy_addr_netloc)
#         except KeyError:
#             pass
#         logger.info("remove failure proxy: {}, left {}".format(proxy_addr, self.proxies))
