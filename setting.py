# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 有效代理返回状态码
VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
CHECKER_CYCLE = 20
# 获取周期
FETCHER_CYCLE = 300

# 测试代理用API，可以换成用要抓取的那个网站来测试
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = 'localhost'
API_PORT = 2018

# 开关
CHECKER_ENABLED = True
FETCHER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
