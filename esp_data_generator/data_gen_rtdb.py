import datetime
import os
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def push_random_data(uid):
    ref = db.reference(f"users/{uid}/sensor_data")
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
    for label in ["humidity", "temperature", "water_level"]:
        label_data = {label: data[label], "timestamp": timestamp.timestamp()}
        ref.child(label).push(label_data)
        print(f"Push data {label_data}")
