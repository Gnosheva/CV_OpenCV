import cv2

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_FREERATIO)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_orig = cv2.imread('men.jpg',1)
# преобразуем изображение к оттенкам серого
img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# инициализировать распознаватель лиц (каскад Хаара по умолчанию)
# обнаружение всех лиц на изображении
faces = face_cascade.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

# печатать количество найденных лиц
print(f"{len(faces)} лиц обнаружено на изображении.")
# для всех обнаруженных лиц рисуем квадрат
for x, y, width, height in faces:
    cv2.rectangle(img_orig, (x, y), (x + width, y + height), color=(0, 255, 0), thickness=2)


viewImage(img_orig, 'res')