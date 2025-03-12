import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
import threading

init()  # Initialize colorama

print_lock = threading.Lock()

def proxy_http():
    urls = [
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
    ]

    def proxies_scrape(urls):
        proxy_dict = {}
        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                proxies = response.text.split('\n')
                for proxy in proxies:
                    if proxy:
                        proxy_dict[proxy] = url
            except requests.RequestException as e:
                print(f"Error fetching proxies from {url}: {e}")
        return proxy_dict

    def check_proxy(proxy, url):
        try:
            response = requests.get("https://www.discord.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            response.raise_for_status()
            with print_lock:
                print(f'{Fore.MAGENTA}{proxy} {Fore.GREEN}[Working] {Fore.BLUE}(source: {url}){Style.RESET_ALL}')
                with open('proxies.txt', 'a') as file5:
                    file5.write(f'{proxy}\n')
            return True
        except requests.exceptions.RequestException:
            with print_lock:
                print(f'{Fore.MAGENTA}{proxy} {Fore.RED}[Not Working] {Fore.YELLOW}(source: {url}){Style.RESET_ALL}')
            return False

    def main():
        valid_proxies = []

        # Scrape the proxies from the URLs
        proxy_dict = proxies_scrape(urls)

        with ThreadPoolExecutor(max_workers=100100) as executor:
            futures = {executor.submit(check_proxy, proxy, url): proxy for proxy, url in proxy_dict.items()}
            for future in as_completed(futures):
                proxy = futures[future]
                if future.result():
                    valid_proxies.append(proxy)

    main()

proxy_http()