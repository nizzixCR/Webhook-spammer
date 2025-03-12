urls = {
    "http": [
        "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/proxyscrape_premium_http_proxies.txt",
        "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/proxies.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/http.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
        "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
    ],
    "https": [
        "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/http_proxies.txt",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/https.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
        "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
    ],
    "socks4": [
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks4.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks4/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/socks4.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
        "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
        "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/socks4_proxies.txt",
        
    ],
    "socks5": [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks5.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks5/socks5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/socks5.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
        "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
        "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/socks5_proxies.txt",
        
    ]
}

import requests
with open("outpy.txt", "w") as outfile:
    for proxy_type, url_list in urls.items():
        for url in url_list:
            try:
                response = requests.get(url)
                response.raise_for_status()
                content = response.text.replace('\r\n', '\n').replace('\r', '\n')
                outfile.write(content)
            except requests.RequestException as e:
                print(f"Error downloading {url}: {e}")