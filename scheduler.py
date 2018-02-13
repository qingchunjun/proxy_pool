import time
from multiprocessing import Process
from api import app
from fetcher import Fetcher
from proxy_checker import ProxyChecker
from setting import *


class Scheduler:
    def schedule_checker(self, cycle=CHECKER_CYCLE):
        """
        定时测试代理
        """
        checker = ProxyChecker()
        while True:
            print('测试器开始运行')
            checker.run()
            time.sleep(cycle)
    
    def schedule_fetcher(self, cycle=FETCHER_CYCLE):
        """
        定时获取代理
        """
        fetcher = Fetcher()
        while True:
            print('开始抓取代理')
            fetcher.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print('代理池开始运行')

        if FETCHER_ENABLED:
            print('启动获取器进程...')
            fetcher_process = Process(target=self.schedule_fetcher)
            fetcher_process.start()

        if CHECKER_ENABLED:
            print('启动测试器进程...')
            checker_process = Process(target=self.schedule_checker)
            checker_process.start()

        if API_ENABLED:
            print('启动API接口服务...')
            api_process = Process(target=self.schedule_api)
            api_process.start()
