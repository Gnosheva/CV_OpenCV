# Взять какую-нибудь фотографию (или самому сделать на телефон). C помощью opencv сделать преобразования:

# Выравнивание гистограммы

# Выравнивание гистограммы — это метод обработки контрастности изображения с использованием гистограммы изображения.
import cv2


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


im = cv2.imread('forest.jpg',)
viewImage(im, 'before')
img_local_hist1 = cv2.imread('facejpg.jpg')
viewImage(img_local_hist1, 'before')

image_yuv = cv2.cvtColor(img_local_hist1, cv2.COLOR_BGR2YUV)
image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:, :, 0])
res = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)
viewImage(res, 'after')

# Локальное выравнивание гистограммы

img_local_hist = cv2.imread('facejpg.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_local_hist)

viewImage(cl1, 'local')
# Гауссовское размытие

img_blur_3 = cv2.GaussianBlur(im, (3, 3), 0)
img_blur_7 = cv2.GaussianBlur(im, (7, 7), 0)
img_blur_11 = cv2.GaussianBlur(im, (11, 11), 0)
viewImage(img_blur_3, 'gauss3')
viewImage(img_blur_7, 'gauss7')
viewImage(img_blur_11, 'gauss11')
# Фильтры Собеля и Лапласа

my_photo = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(my_photo, -1, 1, 0)
sobely = cv2.Sobel(my_photo, -1, 0, 1)
viewImage(sobely, 'sobely')
viewImage(sobelx, 'sobelx')

laplacian = cv2.Laplacian(my_photo, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
viewImage(laplacian, 'laplacian')