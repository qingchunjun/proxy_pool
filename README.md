# proxy_pool

IP proxy pool used by spiders<p>

## 结构示意图
![结构示意图](https://github.com/qingchunjun/proxy_pool/img/architecture.png)


## 本IP代理池框架共分为以下几个部分：<br>

1. 抓取器(crawler.py、fetcher.py)<br>
主要负责抓取指定IP代理网站的代理资源。大家可以自行增加待抓取IP代理网站的抓取方法，自定义的抓取方法必须以"crawl_"开头。
抓取方法增加后，下次启动IP代理池时，将自动抓取这些代理网站的数据。fetcher.py主要负责调用crawler抓取器进行抓取，抓取之前
会判断是否资源池的IP达到上限值。<br>

2. 数据管理器(db.py)<br>
主要负责Redis连接、代理IP资源的存储、IP资源Ranking、排序等操作<br>

3. 检测器(proxy_checker.py)<br>
主要负责以异步IO的方式对Redis中保存的代理进行有效性检测<br>

4. API(api.py)<br>
以Flask web api方式向外部提供代理数据。用户可以自定义服务方法。<br>

5. 调度器(scheduler.py)<br>
主要负责综合调度功能，以进程方式启动各个模块进行工作。<br>

6. 配置文件(settings.py)<br>
相关常量配置<br>


## ======安装方式======<br>

Python3.6<br>
Redis单独安装后，启动Redis服务<br>
其他第三方库可以使用pip安装： pip install -r requirements.txt<br>

安装完毕后，直接运行run.py文件即可<br>

爬虫调用IP代理资源，以HTTP方式进行访问：<br>
import requests<br>

r = requests.get("http://localhost:2018/get")<br>
print(r.text)
