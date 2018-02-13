from utils import get_page
from lxml import etree
import time


class Crawler:

    # 获取Crawler类中所有的爬取方法名
    def get_funclist(self):
        func_list = []
        for k, v in Crawler.__dict__.items():
            if 'crawl_' in k:
                func_list.append(k)
        return func_list

    # 通过反射直接通过方法名调用爬取方法获取代理列表
    def get_proxies(self, func):
        proxies = []
        for proxy in eval("self.{}()".format(func)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=5):
        """
        代理名称：66ip
        :param page_count: 页码
        :return: proxy
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            r = get_page(url)
            html = etree.HTML(r)
            proxy_trs = html.xpath("//div[@id='main']//table//tr")
            for i in range(1, len(proxy_trs)):  # 第一行是标题，略过
                ip = proxy_trs[i].xpath("./td[1]")[0].text
                port = proxy_trs[i].xpath("./td[2]")[0].text
                yield ":".join([ip, port])

    def crawl_ip181(self):
        """
        代理名称：ip181
        :return: proxy
        """
        url = 'http://www.ip181.com/'
        html = etree.HTML(get_page(url))
        proxy_trs = html.xpath("//table//tr[not (@class='active')]")
        for tr in proxy_trs:
            ip = tr.xpath("./td[1]")[0].text
            port = tr.xpath("./td[2]")[0].text
            yield ":".join([ip, port])

    def crawl_kuaidaili(self, page_count=5):
        """
        代理名称：快代理
        :param page_count: 页码
        :return: proxy
        """
        base_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [base_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            time.sleep(1)
            html = etree.HTML(get_page(url))
            proxy_trs = html.xpath("//div[@id='list']/table//tr")
            for i in range(1, len(proxy_trs)):
                ip = proxy_trs[i].xpath("./td[1]")[0].text
                port = proxy_trs[i].xpath("./td[2]")[0].text
                yield ":".join([ip, port])