import configuration
import requests
import data


#создаем заказ
def post_zakaz(body):
    track = requests.post(configuration.URL_SERVICE + configuration.ZAC_NOV, json=data.body).json()['track']
    return track


#выполняем запрос на получение заказа по треку
def get_zakaz_now(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ZAK + str(track))
    response = get_zakaz_now(track)
    print(response.status_code)
    print(response.json())





