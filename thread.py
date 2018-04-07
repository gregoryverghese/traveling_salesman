'''import threading

class swapThread(threading.Thread):

    def __init__(self, road_map):
        threading.Thread.__init__(self):
        self.road_map = road_map
    def run(self):
        find_best_cycle(road_map)
        '''


    #thread.start_new_thread(start_swap_adjacent_thread, (road_map, optimal))
    #thread.start_new_thread(start_swap_cities_thread, (road_map, optimal))
