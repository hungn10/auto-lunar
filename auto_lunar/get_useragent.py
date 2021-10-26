import re,requests,random

def get_ua():
    ua_list = []
    userlist=re.sub('\r\n', '\n', str(requests.get('http://pastebin.com/raw/VtUHCwE6').text)).splitlines()
    for x in userlist:
        ua_list.append(x)
    random.shuffle(ua_list)
    return ua_list
