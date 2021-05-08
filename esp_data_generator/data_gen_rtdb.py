import datetime
import os
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def push_random_data(uid):
    ref = db.reference(f"sensor_data/users")
    user_ref = ref.child(uid)
    humidity = random.randint(100, 1000)
    temperature = random.randint(60, 90)
    waterlevel = random.random() * 10
    timestamp = datetime.datetime.now()
    data = {
        "humidity": humidity,
        "temperature": temperature,
        "water_level": waterlevel,
        "timestamp": timestamp.timestamp(),
        # "timestamp_server": {".sv": "timestamp"},
        # "timestamp_local": timestamp.timestamp()
    }
    user_ref.push(data)
    print(f"Push data {data}")
