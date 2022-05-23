import json
with open("data/sensor.json", "r") as f:
    df = json.load(f)
    print(f"(1) 加速度 {df['sensordata']['accel']}")
    print(f"(2) 光センサの値 {df['sensordata']['light']['light']}")
    print(
        f"(3) タッチした指の位置 {df['sensordata']['touch'][0]['x']},{df['sensordata']['touch'][0]['y']}")
    print(
        f"    タッチした指の位置 {df['sensordata']['touch'][1]['x']},{df['sensordata']['touch'][1]['y']}")
    print(f"(4) timestamp {df['timestamp']}")
