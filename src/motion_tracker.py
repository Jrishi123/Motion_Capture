import cv2
import numpy as np
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--output', default='motion_log.csv')
args = parser.parse_args()

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

with open(args.output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Motion Detected'])

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(prev_frame, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        motion_detected = np.sum(thresh) > 100000

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, 'Yes' if motion_detected else 'No'])
        cv2.imshow('Motion Detection', thresh)
        prev_frame = gray

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
