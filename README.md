## 简介

这是一个爬取lofter文章的小爬虫程序，采用[Scrapy](https://scrapy.org/)框架，更多内容可参考[官方文档](https://docs.scrapy.org/en/latest/)


## 如何使用

1. 修改 `lofter/lofter/spiders/article_spider.py`中的`start_urls`，更改成要爬取的第一个页面，

如:

```python

class LofterArticleSpider(Spider):
    name = "lofter"

    start_urls = [
        "http://{name}.lofter.com/?page=1" # 此处{name}改成你的名字
    ]

```


2. 执行下面命令

```bash
virtualenv -p python3 .env
source .env/bin/activate

pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/

cd lofter/ && mkdir articles
scrapy crawl lofter

```

3. 最终文章将保存在lofter/articles目录下



