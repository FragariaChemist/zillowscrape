# Scrapy settings for zillowscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zillowscraper"

SPIDER_MODULES = ["zillowscraper.spiders"]
NEWSPIDER_MODULE = "zillowscraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zillowscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'zguid=24|%2493a23f51-9f81-4959-9b03-859c2ee53745; zjs_anonymous_id=%2293a23f51-9f81-4959-9b03-859c2ee53745%22; zjs_user_id=null; zg_anonymous_id=%226550e124-01df-4a8f-b191-854257fdc14f%22; _ga=GA1.2.1446318019.1737742904; _pxvid=0278e9bb-da80-11ef-9197-ca6d11243d42; _gcl_au=1.1.811788682.1737742906; _scid=NKo4fX7cuzChr-abn_6C4R-_9PkUlnHg; _tt_enable_cookie=1; _ttp=BQbpfHE7B96Vufh1xS1eYIrcIgx.tt.1; _fbp=fb.1.1737742906447.69642559188535523; _pin_unauth=dWlkPVpUaGhORGhqWlRNdE1UWTJNaTAwTmpreUxUazNZall0T1dZNU1EYzVZMkpqWWpJMQ; _ScCbts=%5B%5D; _sctr=1%7C1737705600000; FSsampler=478331583; web-platform-data=%7B%22wp-dd-rum-session%22%3A%7B%22doNotTrack%22%3Atrue%7D%7D; zgsession=1|ec53f6d4-96e0-4d18-943b-db7aebfa9f47; _gid=GA1.2.604423826.1738015831; AWSALB=cBHLn/QM2kt876yQT/+NLshPTivjtpilM4ws3HyTONEQsABxBPnjD4YcqpxCfciNmJR75yzll35Cjz88DqSoOVmJPIVclT/Ci2tSV8cqFmSb3prnJ9V2yCdwSHvp; AWSALBCORS=cBHLn/QM2kt876yQT/+NLshPTivjtpilM4ws3HyTONEQsABxBPnjD4YcqpxCfciNmJR75yzll35Cjz88DqSoOVmJPIVclT/Ci2tSV8cqFmSb3prnJ9V2yCdwSHvp; JSESSIONID=11218051C45D7630A39085BE43B8D088; pxcts=75d47357-dcfb-11ef-a405-fd477d3c28ed; _rdt_uuid=1737742906170.afe33d92-dd39-441c-9f35-0022f0d2e0f8; _scid_r=QSo4fX7cuzChr-abn_6C4R-_9PkUlnHgWuafJA; DoubleClickSession=true; tfpsi=b8ae6442-2389-4542-802a-b29ed38cca8a; _clck=1xkdp6d%7C2%7Cfsx%7C0%7C1850; __gads=ID=3f4cd0b287d9d732:T=1737742881:RT=1738015805:S=ALNI_Mb6FTt-UD8M8l8yqFNkXD--MfjBxw; __gpi=UID=0000100031415756:T=1737742881:RT=1738015805:S=ALNI_MYcwUt2W87L_QoVzzv1pbamhbnrMQ; __eoi=ID=e104a2d4236ac544:T=1737742881:RT=1738015805:S=AA-AfjafXo3Bra08Jl7IE38cZLZa; search=6|1740607812346%7Crect%3D34.61822556452183%2C-117.92352754394531%2C33.419684041618936%2C-118.89993745605469%26rid%3D12447%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26type%3Dhouse%2Ccondo%2Ctownhouse%2Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26ita%3D0%26stl%3D0%26fur%3D0%26os%3D0%26ca%3D0%26np%3D0%26hasDisabledAccess%3D0%26hasHardwoodFloor%3D0%26areUtilitiesIncluded%3D0%26highSpeedInternetAvailable%3D0%26elevatorAccessAvailable%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912447%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _uetsid=86587970dcfb11ef91b5f9aef15ce400; _uetvid=11e52290da8011ef8459c91c5c9ba04d; _clsk=17f18z7%7C1738015978091%7C7%7C0%7Cj.clarity.ms%2Fcollect; _px3=9c300a36f05baf9019d48c5bd4b97226d4563d3436d011518d6e7e5e1d4b036a:OtU2ToxqmvbB311gn5qrFjB324zoErMxH4lJS35O6cxzrgrWYiMxhS9Av9p59wJTi84QRoVzY6mP5Dh50Velzg==:1000:bCZf/iYi4CVzyK/ZbhUNYdAiIqQrSNxLS/1RbqWIgNCJ2h/uEnDSeKjKKFcGYZ1eCmH62XXnISkoWEMhpTetpbbBB4bPVucGtBEwmjbwUyp0geWuybRiM5+wXqHz9agCf8w4cHa/b3VnIs+R10crvecaANRGMIL9+QaZTYzahBnKOWkwrgkGLdAi8G6Zq0Sg34Cqlo3oKcE2Stez5XW/tiWByChc56RvcVgeMsdZ3/U=',
    'priority': 'u=0, i',
    'referer': 'https://www.zillow.com/los-angeles-ca/rentals/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zillowscraper.middlewares.ZillowscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zillowscraper.middlewares.ZillowscraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zillowscraper.pipelines.ZillowscraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
