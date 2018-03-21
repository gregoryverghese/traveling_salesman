from cities import *

def test_compute_total_distance():

    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, -112.073844)]

    total_distance = 1791
    distance = compute_total_distance(road_map)

    assert distance == total_distance
