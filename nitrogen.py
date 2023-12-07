import requests
import re
import random
import os
import threading
import time
from fake_useragent import UserAgent
from colorama import Style, Fore
from os import system

system('clear')

http_links = [
    "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt"
]

banner = f"""
{Fore.LIGHTBLUE_EX}   _  ___ __           __________  ___   _____ 
  / |/ (_) /________  / ___/ __/ |/ / | / /_  |
 /    / / __/ __/ _ \/ (_ / _//    /| |/ / __/ 
/_/|_/_/\__/_/  \___/\___/___/_/|_/ |___/____/ {Fore.RESET}
"""
good_proxies = set()
print(banner)
print(f"NitroGENV2 Started!")
print(f"Code by root@TibuSpike001 ~#")


class ProxyParser():
    def __init__(self, good_proxies):
        self.good_proxies = good_proxies

    def proxypars(self, url):
        pon = UserAgent()
        r = requests.get(url, headers={'User-Agent': pon.random})
        ip_port = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5})', r.text)
        for proxy in ip_port:
            self.good_proxies.add(proxy)
        print(f"{Fore.GREEN}[+]{Fore.RESET} Proxy donwloads!")

threads = []
for url in http_links:
    proxy_parser = ProxyParser(good_proxies)
    t = threading.Thread(target=proxy_parser.proxypars, args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


class NitroGenCheck():
    def __init__(self, good_proxies, code):
        self.good_proxies = good_proxies
        self.code = code

    def nitrogen(self):
        while True:
            try:
                self.code = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(16))
                r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{self.code}?with_application=false&with_subscription_plan=true', proxies={'http': random.choice(list(self.good_proxies))})
                if r.status_code == 200:
                    print(f"{Fore.GREEN}[+]{Fore.RESET} Valid code ==> https://discord.com/gifts/{self.code}")
                    with open('goodcode.txt', 'a') as f:
                        f.write(self.code + '\n')
                elif r.status_code == 404:
                    print(f'{Fore.RED}[-]{Fore.RESET} Invalid code ==>  https://discord.com/gifts/{self.code}')
                else:
                    print(f'{Fore.RED}[-]{Fore.RESET} Xyeta code ==>  https://discord.com/gifts/{self.code}')
            except:
                pass


for th in range(500):
    nitro_gen_check = NitroGenCheck(good_proxies, None)
    t = threading.Thread(target=nitro_gen_check.nitrogen)
    t.start()

time.sleep(20)
system('clear')
