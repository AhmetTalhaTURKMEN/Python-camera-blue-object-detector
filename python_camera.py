import cv2

# Kamera cihazını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kare alınamadıysa döngüden çık
    if not ret:
        break

    # Görüntüyü BGR renk formatından HSV renk formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi nesneleri tespit etmek için bir HSV aralığı belirle
    lower_blue = (90, 50, 50)
    upper_blue = (130, 255, 255)

    # HSV aralığına göre maske oluştur
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maske üzerindeki kontürleri bul
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Kontürler arasında en büyük olanı bul
    largest_contour = max(contours, key=cv2.contourArea)

    # En büyük kontürün etrafına bir dikdörtgen çiz
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mavi nesne algılandığında bir fotoğraf çek
    if cv2.contourArea(largest_contour) > 1000:
        cv2.imwrite("mavi_nesne_fotografi.jpg", frame)
        break

    # Görüntüyü ekranda göster
    cv2.imshow("Frame", frame)

    # Q tuşuna basarak programı sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bellekten kamera cihazını serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
