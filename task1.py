import cv2
import matplotlib.pyplot as plt
import numpy as np


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def average_brgt(img):
    s =0
    l = 64*64
    for i in range(64):
        s += sum(img[i])
    return np.log10(s/l)

avg_b = []
for i in range(37):
    img_name = "images/"+str(i+1)+".jpg"
    im_gray = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    crop_img = im_gray[2000:2064, 1500:1564]
    avg_b.append(average_brgt(crop_img))



h = -3
ev = []
for i in range(37):
   h += 0.17
   ev.append(np.around(h, decimals = 2))
plt.plot(ev,avg_b)
plt.xlabel('EV')
plt.grid()
plt.show()

