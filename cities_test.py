import pytest
from cities import *
from earth_distance import distance

@pytest.fixture()
def road_map():

    road_map_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, -112.073844)]

    return road_map_list


def test_compute_total_distance(road_map):

    print(road_map)

    total_distance2 = compute_total_distance(road_map)

    assert total_distance2 == pytest.approx(6356, abs=30)

    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974)]

    total_distance = compute_total_distance((road_map1))

    assert total_distance ==  pytest.approx(2970, abs=50)


def test_swap_adjacent_cities(road_map):

    adjusted_road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                        ('Arizona', 'Phoenix', 33.448457, -112.073844),
                        ('Alaska', 'Juneau', 58.301935, -134.41974)]

    new_road_map_tuple = swap_adjacent_cities(road_map, index=1)

    new_road_map = new_road_map_tuple[0]
    new_distance = new_road_map_tuple[1]

    assert new_road_map == adjusted_road_map
    assert new_distance == pytest.approx(2000, abs=50)
