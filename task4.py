import cv2
import numpy as np

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

apple_path = 'apple.jpg'
orange_path = 'orange.jpg'

apple = cv2.imread(apple_path)
orange = cv2.imread(orange_path)

# печать формы  изображений
print(apple.shape)
print(orange.shape)
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#пирамида Гаусса для яблока
apple_copy = apple.copy()  # копия изображения для яблока
gp_apple = [apple_copy]  # создание пирамиду Гаусса как список
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#пирамида Гаусса для апельсина
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
     orange_copy = cv2.pyrDown(orange_copy)
     gp_orange.append(orange_copy)

# пирамида Лапласса для аблока
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
     gaussian_expanded = cv2.pyrUp(gp_apple[i])
     laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
     lp_apple.append(laplacian)
#для апельсина
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
     gaussian_expanded = cv2.pyrUp(gp_orange[i])
     laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
     lp_orange.append(laplacian)

#функция zip для объединения пирамиды яблока и апельсина
#добавляем левую и праву половину изобрадений на каждом уровне
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
     n += 1
     cols, rows, ch = apple_lap.shape
     laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))#деление столбцов обоих изображений пополам
     apple_orange_pyramid.append(laplacian)#добавление переменной в список

#реконструируем  изображение, используя pyrUp и указывая уровни пирамиды
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
     apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
     apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)



viewImage(apple_orange_reconstruct, 'res')
