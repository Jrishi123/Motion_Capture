\# 🎥 Linux Motion Capture Using OpenCV \& MoCap Camera



This project demonstrates how to interface a motion capture (MoCap) camera system on a Linux environment using OpenCV and other tools. It captures real-time video, tracks motion, logs data, and enables optional 3D pose tracking.



\## 📌 Features

\- Real-time motion stream using OpenCV

\- Basic motion tracking using frame differencing

\- Logs motion activity with timestamps

\- Supports Intel RealSense, USB cams, and virtual MoCap devices

\- Simple shell scripts for environment setup



\## 🧰 Tech Stack

\- OS: Ubuntu 20.04 / Raspberry Pi OS

\- Language: Python 3

\- Libraries: OpenCV, NumPy

\- Tools: FFmpeg, V4L2, Shell

## 🚀 Quick Start (Windows)

To quickly launch the motion tracker on Windows:

1. Clone the repository
2. Double-click `run_motion.bat`
3. Press `q` in the OpenCV window to stop

This will save logs to `motion_log.csv`



\## 🔧 Setup

```bash

sudo apt update \&\& sudo apt install python3-opencv ffmpeg v4l-utils

pip3 install numpy

bash utils/install\_deps.sh



