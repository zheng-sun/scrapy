# -*- coding: utf-8 -*-

# Scrapy settings for kaola project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kaola'

SPIDER_MODULES = ['kaola.spiders']
NEWSPIDER_MODULE = 'kaola.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# Obey robots.txt rules
# 遵守robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# scrapy 执行的最大并发数(默认值:16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟（默认:0秒）
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 每个域名请求并发数
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 每个IP请求并发数
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用cookie(默认启用)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用Telnet控制台(默认启用)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#　覆盖默认请求头　(注：User-Agent不能写到这里)
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#　启用或禁用spider中间件
#SPIDER_MIDDLEWARES = {
#    'kaola.middlewares.KaolaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# 启用或禁用downloader中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'kaola.middlewares.KaolaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
#　启用或禁用扩展
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
#  配置项目管道
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'kaola.pipelines.KaolaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
#　启用并配置自动节流阀扩展(默认禁用)　防止请求过快，将服务器抓崩。
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#　启用和配置HTTP缓存（默认禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

