import datetime
import random
import time
import sys

import data_gen

if __name__ == "__main__":
    target_uid = sys.argv[1]

    min_wait_sec = 5
    max_wait_sec = 15

    max_iterations = 15

    for i in range(max_iterations):
        waiting = random.random() * (max_wait_sec - min_wait_sec) + min_wait_sec
        time.sleep(waiting)
        data_gen.push_random_data(target_uid, datetime.datetime.now())
