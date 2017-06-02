import requests
import json

class RestaurantApiMaker:
    def __init__(self, latitude, longitude):
        self.api_url = 'https://mainsite-restapi.ele.me/shopping/restaurants?' \
                       'latitude={}&longitude={}'.format(latitude, longitude)

    def get_url(self, offset, limit):
        return self.api_url + '&offset={}&limit={}'.format(offset, limit)

url_maker = RestaurantApiMaker(32.119004, 118.928748)
url = url_maker.get_url(10, 20)
req = requests.request("GET", url)
json_str = req.content
json_str = json_str.decode('utf-8')
json_obj = json.loads(json_str)
for obj in json_obj:
    print(obj)

