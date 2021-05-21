from datetime import datetime, timedelta
import os
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np


def push_random_data(uid):
    ref = db.reference(f"users/{uid}/sensor_data")
    user_ref = ref.child(uid)
    humidity = random.randint(20, 100)
    humidity = np.random.normal(loc=75, scale=4)
    temperature = np.random.normal(loc=70, scale=8)
    waterlevel = np.random.normal(loc=7, scale=0.7)
    timestamp = datetime.now()
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
