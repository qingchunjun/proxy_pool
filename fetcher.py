from db import RedisClient
from crawler import Crawler
from setting import *
import sys


class Fetcher:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        """
        判断是否达到了代理池数量上限
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for func in self.crawler.get_funclist():
                # 从各个代理IP网站开始获取IP代理地址
                proxies = self.crawler.get_proxies(func)
                sys.stdout.flush()
                for proxy in proxies:
                    # 将获取的proxy加入到redis队列
                    self.redis.add(proxy)
