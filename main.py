import re,requests,random
from time import sleep
from auto_lunar import auto, get_useragent, proxy
import threading

#ua_list = get_useragent.get_ua()
#random.choice(ua_list)
#proxy = proxy.check_ip()
with auto.auto() as driver:
    driver.get('https://lunarcrush.com/')
    sleep(30)
    driver.create_account('congchua@gmail.com')
