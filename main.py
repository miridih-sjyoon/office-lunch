import datetime

from restaurant import Restaurant

if __name__ == '__main__':
    print(datetime.datetime.now())
    for restaurant in list(Restaurant):
        print(restaurant.name, restaurant.get_menu())
