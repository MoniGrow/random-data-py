import datetime
import random
import time

import data_gen

if __name__ == "__main__":
    target_uid = "bB1jtMSXS3U6NVN62lu0l4gGqci1"

    min_wait_sec = 5
    max_wait_sec = 15

    while True:
        waiting = random.random() * (max_wait_sec - min_wait_sec) + min_wait_sec
        time.sleep(waiting)
        data_gen.push_random_data(target_uid, datetime.datetime.now())
        print("")
