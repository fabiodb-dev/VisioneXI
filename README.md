# VisioneXI

Computer vision system for detecting and tracking football players from match footage.

## Demo

![Demo](demo/demo.gif)

## Overview

The goal is to build a pipeline capable of extracting useful information from match footage, such as player positions and movement patterns.

## Features

- Player detection using YOLO
- Frame-by-frame video processing
- Bounding box visualization
- Detection confidence score

Future improvements will include:

- Player tracking across frames
- Ball detection
- Team classification
- Movement statistics

## Technologies

- Python
- OpenCV
- YOLO (ultralytics)
- NumPy

## How it works

1. A football match video is loaded.
2. Each frame is processed using a YOLO model.
3. Players are detected and bounding box are drawn.
4. The processed frames are saved into a new video.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/fabiodb-dev/VisioneXI.git
cd VisioneXI
```

### 2. Create a virtual environment

It is reccomended to run the project inside a Python virtual environment.

```bash
python3 -m venv venv
```

Activate it:
 - Linux/MacOS:
```bash
   source venv/bin/activate
```
 - Windows:
 ```bash
    venv/Scripts/activate
```

### 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Verify installation:

Run the track script:
```bash
python track.py
```
If everything is set up correctly, the script should start processing the input video.
