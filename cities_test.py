import pytest
from cities import *
from earth_distance import distance

@pytest.fixture()
def road_map():

    road_map_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, -112.073844),
                ('Arkansas', 'Little Rock',	34.736009, -92.331122)]

    return road_map_list


def test_compute_total_distance(road_map):

    total_distance2 = compute_total_distance(road_map)

    assert total_distance2 == pytest.approx(6372, abs=30)



def test_compute_total_distance_two_locations():

    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974)]

    total_distance = compute_total_distance((road_map1))

    assert total_distance ==  pytest.approx(2870, abs=50)



def test_swap_adjacent_cities(road_map):

    adjusted_road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                        ('Arizona', 'Phoenix', 33.448457, -112.073844),
                        ('Alaska', 'Juneau', 58.301935, -134.41974),
                        ('Arkansas', 'Little Rock',	34.736009, -92.331122)]

    new_road_map_tuple = swap_adjacent_cities(road_map, index=1)

    new_road_map = new_road_map_tuple[0]
    new_distance = new_road_map_tuple[1]

    assert new_road_map == adjusted_road_map
    assert new_distance == pytest.approx(6397, abs=50)


def test_swap_cities(road_map):

        road_map_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                    ('Arkansas', 'Little Rock',	34.736009, -92.331122),
                    ('Arizona', 'Phoenix', 33.448457, -112.073844),
                    ('Alaska', 'Juneau', 58.301935, -134.41974)]

        new_road_map_tuple = swap_cities(road_map, index1=1, index2=3)

        new_road_map = new_road_map_tuple[0]
        new_distance = new_road_map_tuple[1]

        assert new_road_map == adjusted_road_map
        assert new_distance == pytest.approx(6372, abs=30)



    #385.07
    #1131.28
    #2004.89
    #2851.48







#385.07
#2004.89
#1494.31
#2512.55
