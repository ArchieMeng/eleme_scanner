import requests
import json


class ElemeApi:
    GEO_RESTAURANT_LIST_API = 'https://mainsite-restapi.ele.me/shopping/restaurants?' \
                        'latitude={latitude}&longitude={longitude}&offset={offset}&limit={limit}'
    GEO_INFO_API = "https://mainsite-restapi.ele.me/bgs/poi/reverse_geo_coding?" \
                   "latitude={latitude}&longitude={longitude}"
    RESTAURANT_MENU_API = "https://mainsite-restapi.ele.me/shopping/v2/menu?restaurant_id={restaurant_id}"
    RESTAURANT_SCORE_API = "https://mainsite-restapi.ele.me/ugc/v2/restaurants/{restaurant_id}/ratings/scores"
    RESTAURANT_FEEDBACK_TAG_API = "https://mainsite-restapi.ele.me/ugc/v2/restaurants/{restaurant_id}/ratings/tags"
    RESTAURANT_BASE_INFO_API = "https://mainsite-restapi.ele.me/shopping/restaurant/{restaurant_id}?" \
                               "extras[]=activities&extras[]=albums&extras[]=license&extras[]=identification" \
                               "&latitude={latitude}&longitude={longitude}"
    UA = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6,zh;q=0.4',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'mainsite-restapi.ele.me',
        'Origin': 'https://h5.ele.me',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/58.0.3029.110 Safari/537.36'
    }

    @staticmethod
    def get_geohash(latitude, longitude):
        """
        Get geography info of given location.
        Geo information includes geohash, location name and city & city_id.
        :param latitude: float number of latitude
        :param longitude:float number of longitude
        :return: JSON object of Geo Info
        """
        request_url = ElemeApi.GEO_INFO_API.format(latitude=latitude, longitude=longitude)
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj

    @staticmethod
    def __get_json_obj__(url, headers=None):
        """
        internal method to get json object with header
        :param url: request JSON object url
        :param headers: dictionary of header . if not set, default headers will be used
        :return: JSON object
        """
        if headers:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=ElemeApi.UA)

        json_str = response.content.decode('utf-8')
        json_obj = json.loads(json_str)
        return json_obj

    @staticmethod
    def get_restaurants_by_location(
            latitude=32.119,
            longitude=118.928,
            offset=0,
            limit=0
    ):
        """
        Get list of restaurants by given geography locations
        :param latitude: float number of latitude
        :param longitude:float number of longitude
        :param offset: number of restaurants to ignore from the beginning
        :param limit: number of restaurants to want
        :return: JSON object of restaurants list
        """
        request_url = ElemeApi.GEO_RESTAURANT_LIST_API.format(
            latitude=latitude,
            longitude=longitude,
            offset=offset,
            limit=limit
        )
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj

    @staticmethod
    def get_restaurant_menu(restaurant_id):
        """
        get foods menu of restaurant of given restaurant_id
        :param restaurant_id: int
        :return:
        """
        request_url = ElemeApi.RESTAURANT_MENU_API.format(restaurant_id=restaurant_id)
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj

    @staticmethod
    def get_restaurant_score(restaurant_id):
        """
        get score data of restaurant
        :param restaurant_id: int
        :return: JSON object
        """
        request_url = ElemeApi.RESTAURANT_SCORE_API.format(restaurant_id=restaurant_id)
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj

    @staticmethod
    def get_restaurant_feedback_tags(restaurant_id):
        """
        get customer feedback tag count data
        :param restaurant_id: int
        :return: JSON object
        """
        request_url = ElemeApi.RESTAURANT_FEEDBACK_TAG_API.format(restaurant_id=restaurant_id)
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj

    @staticmethod
    def get_restaurant_basic_info(
            restaurant_id,
            latitude=32.119,
            longitude=118.928
    ):
        """
        get basic info of restaurant
        :param restaurant_id: int
        :param latitude: float
        :param longitude: float
        :return:
        """
        request_url = ElemeApi.RESTAURANT_BASE_INFO_API.format(
            restaurant_id=restaurant_id,
            latitude=latitude,
            longitude=longitude
        )
        json_obj = ElemeApi.__get_json_obj__(request_url)
        return json_obj
