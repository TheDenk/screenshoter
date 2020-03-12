#python3 screenshoter.py -i {path_to_folder}

import os
import glob
import argparse

import cv2
import keyboard as k
import autopy


def main():
    parser = argparse.ArgumentParser(
        description="Help save screenshots in the folder.")
    parser.add_argument("-i",
                        "--images_dir",
                        required=True,
                        help="Path to the folder with images.",
                        type=str)
    args = parser.parse_args()

    image_counts = 0

    files = glob.glob(args.images_dir + '/*')

    if len(files) > 0:
        nums = []
        for file in files:
            nums.append(int(os.path.basename(file).split('.')[0]))
        nums = sorted(nums)
        image_counts = nums[-1]
    print(image_counts)

    while(True):
        if k.is_pressed('shift'):
            img_name = str(image_counts) + '.png'
            img = autopy.bitmap.capture_screen()
            img = np.fromstring(img, dtype='uint8').reshape((h, w, 3))

            file_path = os.path.join(args.images_dir, img_name)
            cv2.imwrite(file_path, img)
            print('image {} is grabbed.'.format(img_name))
            image_counts += 1
        elif k.is_pressed('esc'):
            break


if __name__ == '__main__':
    main()
