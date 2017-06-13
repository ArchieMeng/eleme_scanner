from eleme.api import ElemeApi


def print_shops():
    shop_list = ElemeApi.get_restaurants_by_location(limit=20)
    for shop in shop_list:
        print("-----------------------------{}--------------------------".format(shop['name']))
        for key in shop:
            print("{}:{}".format(key, shop[key]))
    return shop_list


def print_menu(restaurant_id):
    menu = ElemeApi.get_restaurant_menu(restaurant_id)
    for category in menu:
        for key in category:
            print("{}:{}".format(key,category[key]))


if __name__ == "__main__":
    # get geo info
    geo_info = ElemeApi.get_geohash(latitude=32.119, longitude=118.928)
    print(geo_info)

    # get shop list
    shop_list = print_shops()

    # get shop menu
    print()
    print()
    print_menu(shop_list[0]['id'])

    # get rate
    print(ElemeApi.get_restaurant_score(shop_list[0]['id']))
    print(ElemeApi.get_restaurant_feedback_tags(shop_list[0]['id']))

    # get basic info
    print(ElemeApi.get_restaurant_basic_info(shop_list[0]['id']))