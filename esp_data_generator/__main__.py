import datetime
import os
import random
import time
import sys

import firebase_admin
from firebase_admin import credentials

import data_gen_firestore
import data_gen_rtdb

if __name__ == "__main__":
    if not firebase_admin._apps:
        cert_path = "~/Documents/Programs/fellowship/monigrow-a9692-firebase-adminsdk-ww1uk-eca9f620c2.json"
        cred = credentials.Certificate(os.path.expanduser(cert_path))
        firebase_admin.initialize_app(cred, {
            'projectId': "monigrow-a9692",
            "databaseURL": "https://monigrow-a9692-default-rtdb.firebaseio.com/"
        })
    db_type = sys.argv[1]
    if db_type not in ("firestore", "rtdb"):
        raise ValueError(f"{db_type} is not 'firestore' or 'rtdb'")
    target_uid = sys.argv[2]

    min_wait_sec = 5
    max_wait_sec = 15

    max_iterations = 15

    for i in range(max_iterations):
        waiting = random.random() * (max_wait_sec - min_wait_sec) + min_wait_sec
        time.sleep(waiting)
        if db_type == "firestore":
            data_gen_firestore.push_random_data(target_uid)
        else:
            data_gen_rtdb.push_random_data(target_uid)
