from flask import Flask, g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/get')
def get_proxy():
    """
    随机获取一个代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.get_proxy_by_random()


@app.route('/score/<score>')
def get_proxy_by_score(score):
    """
    按照给定的分值查找对应的所有代理资源
    :param score: 给定的分值条件
    :return: 符合条件的代理列表
    """
    conn = get_conn()
    return '<h2>分数为:' + score + '的代理</h2><br>' + '<br>'.join(conn.get_proxy_by_score(score))


@app.route('/count')
def get_counts():
    """
    获取当前代理池中代理的总量
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())
