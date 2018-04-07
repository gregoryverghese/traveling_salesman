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



def test_compute_total_distance_two_location0s():

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

        adjusted_road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                    ('Arkansas', 'Little Rock',	34.736009, -92.331122),
                    ('Arizona', 'Phoenix', 33.448457, -112.073844),
                    ('Alaska', 'Juneau', 58.301935, -134.41974)]

        new_road_map_tuple = swap_cities(road_map, index1=1, index2=3)

        new_road_map = new_road_map_tuple[0]
        new_distance = new_road_map_tuple[1]

        assert new_road_map == adjusted_road_map
        assert new_distance == pytest.approx(6372, abs=30)


def test_swap_cities_index1_equals_index2(road_map):

        new_road_map_tuple = swap_cities(road_map, index1=1, index2=1)

        new_road_map = new_road_map_tuple[0]
        new_distance = new_road_map_tuple[1]

        assert new_road_map == road_map
        assert new_distance == pytest.approx(6372, abs=30)


def test_find_best_cycle(road_map):

    longer_roadmap = [('California', 'Sacramento', 38.555605,-121.468926),
                    ('Colorado', 'Denver', 39.7391667, -104.984167),
                    ('Connecticut', 'Hartford', 41.767, -72.677),
                    ('Delaware', 'Dover', 39.161921, -75.526755)]

    longer_roadmap.extend(road_map)

    road_map_distance = compute_total_distance(longer_roadmap)

    new_road_map_tuple  = find_best_cycle(longer_roadmap)

    new_road_map = new_road_map_tuple[0]
    new_distance = new_road_map_tuple[1]

    print(road_map_distance)
    print(new_distance)

    assert new_road_map != longer_roadmap
    #assert new_distance < road_map_distance


def start_swap_cities_threads(road_map):


    longer_roadmap = [('California', 'Sacramento', 38.555605,-121.468926),
                    ('Colorado', 'Denver', 39.7391667, -104.984167),
                    ('Connecticut', 'Hartford', 41.767, -72.677),
                    ('Delaware', 'Dover', 39.161921, -75.526755)]

    longer_roadmap.extend(road_map)

    road_map_distance = compute_total_distance(longer_roadmap)

    new_road_map_tuple  = find_best_cycle(longer_roadmap)

    new_road_map = new_road_map_tuple[0]
    new_distance = new_road_map_tuple[1]

    print(road_map_distance)
    print(new_distance)

    assert new_road_map != longer_roadmap
    assert new_distance < road_map_distance


def start_swap_adjacent_threads(road_map):

    longer_roadmap = [('California', 'Sacramento', 38.555605,-121.468926),
                    ('Colorado', 'Denver', 39.7391667, -104.984167),
                    ('Connecticut', 'Hartford', 41.767, -72.677),
                    ('Delaware', 'Dover', 39.161921, -75.526755)]

    longer_roadmap.extend(road_map)

    road_map_distance = compute_total_distance(longer_roadmap)

    new_road_map_tuple  = find_best_cycle(longer_roadmap)

    new_road_map = new_road_map_tuple[0]
    new_distance = new_road_map_tuple[1]

    print(road_map_distance)
    print(new_distance)

    assert new_road_map != longer_roadmap
    assert new_distance < road_map_distance


def test_2opt(road_map):

        longer_roadmap = [('California', 'Sacramento', 38.555605,-121.468926),
                        ('Colorado', 'Denver', 39.7391667, -104.984167),
                        ('Connecticut', 'Hartford', 41.767, -72.677),
                        ('Delaware', 'Dover', 39.161921, -75.526755)]

        longer_roadmap.extend(road_map)
        road_map_distance = compute_total_distance(longer_roadmap)

        new_road_map = opt2(longer_roadmap)

        new_distance = compute_total_distance(new_road_map)
        print(road_map_distance)
        print(new_distance)
        print(new_road_map)

        assert new_road_map != longer_roadmap
        assert new_distance < road_map_distance













    #385.07
    #1131.28
    #2004.89
    #2851.48







#385.07
#2004.89
#1494.31
#2512.55
