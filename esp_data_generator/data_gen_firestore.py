import datetime
import os
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


user_collection = "ESP32data"
sensor_collection = "sensorData"


def get_user_collection(db, uid):
    return db.collection(user_collection).document(uid).collection(sensor_collection)


def push_random_data(uid):
    db = firestore.client()
    humidity = random.randint(100, 1000)
    temperature = random.randint(60, 90)
    waterlevel = random.random() * 10
    # timestamp = firestore.SERVER_TIMESTAMP
    timestamp = datetime.datetime.now()
    data = {
        "humidity": humidity,
        "temperature": temperature,
        "water_level": waterlevel,
        "timestamp": timestamp
    }
    get_user_collection(db, uid).document(str(timestamp)).set(data)
    print(f"Push data {data}")
