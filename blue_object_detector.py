import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)

# Mavi renginin alt ve üst sınırlarını belirle
lower_blue = (100, 50, 50)
upper_blue = (130, 255, 255)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renginin sınırlarına göre bir maske oluştur
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Mavi nesneyi içine alan bir dikdörtgeni çiz
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Görüntüyü göster
    cv2.imshow('frame', frame)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şeyi temizle
cap.release()
cv2.destroyAllWindows()
