#WEB SCRAPING
#API-application programming interface
#PACKAGES
# requests(BASIC PACKAGE)
# bs4(BASIC PACKAGE) (py -m pip install requests --user)-THIS IS HOW YOU INSTALL THESE PACKAGES
# selenium-requires chromium or firefox driver(ADVANCED)
# scrapy(ADVANCED)

#JSON
import requests
class DeviceTracker:
    def __init__(self,ip_url):
        self.ip_url=ip_url
    def get_device_data(self):
        req_data=requests.get(url=self.ip_url)
        if(req_data.status_code==200):
            req_json=req_data.json()
        else:
            req_json={}
        return req_json
ip_url='http://ip-api.com/json/?fields=6143'
ip_dev=DeviceTracker(ip_url=ip_url)
dev_data=ip_dev.get_device_data()
print(dev_data)
