import pytest
from cities import *
from earth_distance import distance


def test_compute_total_distance():

    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                    ('Alaska', 'Juneau', 58.301935, -134.41974)]

    total_distance = compute_total_distance((road_map))

    assert total_distance ==  pytest.approx(2850, 50)

    road_map2 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, -112.073844)]


    total_distance2 = compute_total_distance(road_map2)

    print(total_distance2)

    assert total_distance2 == pytest.approx(6356, abs=30)
