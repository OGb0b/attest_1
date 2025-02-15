from main import Delivery, Stack, Company


def test_add_delivery():
    deliveries = Company()
    deliveries.add_delivery(['123', 'Казань', 'Москва', '10', '100'], 0)
    assert deliveries[0].track_number == 123
    assert deliveries[0].point_of_departure == 'Казань'
    assert deliveries[0].point_of_destination == 'Москва'
    assert deliveries[0].weight == 10
    assert deliveries[0].time == 100


def test_quick_sort_by_time():
    deliveries = Company()
    deliv_1 = ['123', 'Казань', 'Москва', '10', '100']
    deliveries.add_delivery(deliv_1, 0)
    deliv_2 = ['12', 'Лондон', 'Краснодар', '1', '7']
    deliveries.add_delivery(deliv_2,1)
    assert deliveries[0] == deliv_2
    assert deliveries[1] == deliv_1

def test_linear_search_by_track_number():
    deliveries = Company()
    deliv_1 = ['123', 'Казань', 'Москва', '10', '100']
    deliveries.add_delivery(deliv_1, 0)
    deliv_2 = ['12', 'Лондон', 'Краснодар', '1', '7']
    deliveries.add_delivery(deliv_2,1)
    assert deliveries.linear_search_by_track_number(deliv_2[0]) == deliv_2


