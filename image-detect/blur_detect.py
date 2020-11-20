from PIL import Image
import pytesseract
import cv2
import os

# Duong dan den file anh
image_file = './images/77_0.jpg'
# Dinh nghia blur threshold
blur_threshold=100

# # Doc anh tu file
image = cv2.imread(image_file)

if image is None:
    print("Nothing to work!")
else:
    #  chuyển về ảnh xám, sau đó phân tách thành ảnh đen trắng
    gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]

    file = "{}.jpg".format(os.getpid())
    cv2.imwrite(file, gray)

    # Tinh toan muc do focus cua anh
    focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()

    if focus_measure < blur_threshold:
        text = "Blurry pix"
        cv2.putText(image, "{} - FM = {:.2f}".format(text, focus_measure), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    else:
        text = "Fine pix"
        cv2.putText(image, "{} - FM = {:.2f}".format(text, focus_measure), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # # Hien thi anh
    # cv2.imshow("Image", image)
    # key = cv2.waitKey(0)

    to_text = pytesseract.image_to_string(Image.open(file),lang='vie')
    os.remove(file)
    print(to_text)