import sender_stand_request
import data

#Лемешева Наталья 9 когорта Финальный проект. Инженер по тестированию плюс.
def post_zacaz():
    response = sender_stand_request.post_zakaz(data.body)
    return response.json()['track']


def test_get_zakaz_now():
    track = sender_stand_request.post_zakaz(data.body)
    print(track)
    act = sender_stand_request.get_zakaz_now(track)
    print(act.status_code)
    print(act.json())
    exp = 200
    assert act.status_code == 200




