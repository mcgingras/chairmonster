"""
Viz.py

this script listens to the firebase db and constantly polls for changes.
if it hears a change, it reads that value, and renders an appropriate visualization.
"""

import pyrebase
import subprocess

config = {
  "apiKey": "AIzaSyCznH9t2il2tXzSXyf3_SRFEUlbZ3jCREg",
  "authDomain": "mixi-43ed3.firebaseapp.com",
  "databaseURL": "https://mixi-43ed3.firebaseio.com",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    data = message['data']
    if None: # if you delete obj it returns none in the stream...
        return None

    classType = list(data.values())[0]['type']
    showChair() if classType == 1 else showSofa() # dude how can you not love python this literally reads like english


def showChair():
    print('we are showing a chair')
    subprocess.call(['python','/Users/mcgingras/IDEO/Summer18/Build/Boston/chairs/3dgan-release/visualization/python/visualize.py','./3dgan-release/visualization/python/chair_demo.mat', '-u', '0.9', '-t', '0.1', '-i', '1', '-mc', '2'])


def showSofa():
    print('we are showing a sofa')
    subprocess.call(['python','/Users/mcgingras/IDEO/Summer18/Build/Boston/chairs/3dgan-release/visualization/python/visualize.py','./3dgan-release/visualization/python/chair_demo.mat', '-u', '0.9', '-t', '0.1', '-i', '1', '-mc', '2'])
    

my_stream = db.child('demo').stream(stream_handler)
