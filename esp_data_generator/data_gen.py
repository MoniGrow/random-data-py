import datetime
import os
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cert_path = "~/Documents/Programs/fellowship/monigrow-a9692-firebase-adminsdk-ww1uk-eca9f620c2.json"
cred = credentials.Certificate(os.path.expanduser(cert_path))
firebase_admin.initialize_app(cred, {
    'projectId': "monigrow-a9692"
})

db = firestore.client()

user_collection = "ESP32data"
sensor_collection = "sensorData"


def get_user_collection(uid):
    return db.collection(user_collection).document(uid).collection(sensor_collection)


def get_latest_timestamp(uid):
    latest = list(get_user_collection(uid).order_by("timeStamp", direction=firestore.Query.DESCENDING).limit(1).stream())
    if len(latest) == 0:
        return None
    latest = latest[0]
    return latest.to_dict()["timeStamp"]


def push_random_data(uid, timestamp):
    if not isinstance(timestamp, datetime.datetime):
        raise TypeError("timestamp is not a datetime")
    humidity = random.randint(100, 1000)
    temperature = random.randint(60, 90)
    waterlevel = random.random() * 10
    data = {
        "humidity": humidity,
        "temperature": temperature,
        "waterlevel": waterlevel,
        "timestamp": timestamp
    }
    get_user_collection(uid).document(str(timestamp)).set(data)
    print(f"Push data {data}")
