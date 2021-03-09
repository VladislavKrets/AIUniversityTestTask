import sys
import history
import time
import numpy as np


def current_time_millis():
    return round(time.time() * 1000)


def history_test():
    total_size = 0
    list_size = sys.getsizeof(total_size) * 500
    history_entity = history.History()
    first_time_label = current_time_millis()
    total_size = fill_history(history_entity, list_size, total_size, 300000000)
    last_time_label = current_time_millis()
    print("Function worked on first step for", (last_time_label - first_time_label), 'ms')
    print("Duplicates on first step count:", history_entity.duplicates_count)
    print("Saving to disk and loading")
    first_time_label = current_time_millis()
    history_entity.save_history("dump")
    history_entity.load_history("dump")
    last_time_label = current_time_millis()
    print("Function worked on saving and loading for", (last_time_label - first_time_label), 'ms')
    first_time_label = current_time_millis()
    total_size = fill_history(history_entity, list_size, total_size, 500000000)
    last_time_label = current_time_millis()
    print("Function worked on second step for", (last_time_label - first_time_label), 'ms')
    print("Duplicates on second step count:", history_entity.duplicates_count)


def fill_history(history_entity, list_size, total_size, max_size):
    while total_size <= max_size:
        sequence = np.random.randint(1, 50, size=500)
        score = np.random.randint(1, 400)
        history_entity.set_history(sequence, score)
        total_size += list_size
    return total_size


history_test()
