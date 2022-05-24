import cv2

img = cv2.imread("person.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Over the Clouds", img)
cv2.imshow("Over the Clouds - gray", gray)

dst = cv2.blur(img, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
cv2.imshow("Over the Clouds - blur", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('blah')