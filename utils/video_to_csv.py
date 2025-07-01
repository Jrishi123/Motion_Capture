import cv2
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
args = parser.parse_args()

cap = cv2.VideoCapture(args.input)
frame_id = 0

with open('video_motion_log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frame', 'Timestamp'])

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([frame_id, timestamp])
        frame_id += 1

cap.release()
print("Video data logged to video_motion_log.csv")
