from utils import get_page
from lxml import etree
import time
import requests,re

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

    def crawl_ipxici(self):
        """
        代理名称：xicidaili
        :param
        :return: proxy
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        }

        resp = requests.get("https://www.xicidaili.com/nn/", headers=headers)
        ips = re.findall(
            '<td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s+<td>(.*?)</td>\s+<td>(.*?)</td>',
            resp.text, re.S)
        for ip, port in ips:
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
