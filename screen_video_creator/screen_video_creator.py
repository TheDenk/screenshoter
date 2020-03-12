#python3 screen_video_creator.py --name {video_name} --height 1080 --width 1920

import os
import time
import argparse

import cv2
import numpy as np
import keyboard
import autopy


RUN = False
SAVE_AND_EXIT = False


def change_run(value):
    global RUN
    RUN = value


def save_and_exit():
    global SAVE_AND_EXIT
    SAVE_AND_EXIT = True


keyboard.add_hotkey('f6', lambda: change_run(True))
keyboard.add_hotkey('f8', lambda: change_run(False))
keyboard.add_hotkey('f9', lambda: save_and_exit())

def main():
    parser = argparse.ArgumentParser(
        description="Create video from screen.")

    parser.add_argument("-n",
                        "--name",
                        required=True,
                        help="Path to the folder with images.",
                        type=str)

    parser.add_argument("--height",
                        required=False,
                        help="Image height. (Optional)",
                        default=600,
                        type=int)

    parser.add_argument("--width",
                        required=False,
                        help="Image width. (Optional)",
                        default=800,
                        type=int)

    args = parser.parse_args()

    file_name = args.name
    h, w = args.height, args.width
    fps = 20

    writer = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))
    
    while not SAVE_AND_EXIT:
        if RUN:
            img = autopy.bitmap.capture_screen()
            original_w, original_h = autopy.screen.size()
            img = np.fromstring(img, dtype='uint8').reshape((int(original_h), int(original_w), 3))
            img = cv2.resize(img, (w, h))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            writer.write(img)
    
    writer.release()
    

if __name__ == '__main__':
    main()
