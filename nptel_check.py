from PIL import Image
import numpy as np
import glob
import os
import cv2

QR_FILE_PATH = './qrcodes'

if not(os.path.exists(QR_FILE_PATH)):
        os.mkdir(QR_FILE_PATH)

def open_image(file_path : str):
    types = ('*.jpeg', '*.png', '*.jpg')
    for files in types:
        for im_path in enumerate(glob.glob(file_path + files)):
            im_frame = Image.open(im_path[1])
            np_frame = np.array(im_frame).reshape(5029,7009,3)

            img_arr = np_frame.copy()
            img_arr= img_arr[4640:4994, 3585:3935]

            im = Image.fromarray(img_arr)
            im.save(f'{QR_FILE_PATH}/qr{im_path[0]}.png')

    return QR_FILE_PATH


def generate_result(file_path : str):
    qr_link_li=[]
    detector = cv2.QRCodeDetector()

    for im_path in glob.glob(file_path + '/*.png'):
        img = cv2.imread(im_path)
        results = detector.detectAndDecode(img)
        qr_link_li.append(results[0])
    return qr_link_li

res_li = generate_result(open_image('./'))

for i in res_li:
    print(i)