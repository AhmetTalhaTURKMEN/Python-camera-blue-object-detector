import cv2

# Webcam'i başlat
cap = cv2.VideoCapture(0)

# Mavi renk kodunu belirle
blue_lower = (100, 50, 50)
blue_upper = (130, 255, 255)

# Kamerada mavi cisim algılanana kadar bekle
while True:
    # Kameradan bir frame al
    ret, frame = cap.read()
    
    # Renk uzayını HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Mavi renk aralığına uyan maske oluştur
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    
    # Maske üzerinde morfolojik işlemler uygula
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Maskeyi kullanarak mavi cisimleri bul
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Eğer mavi cisim varsa, fotoğraf çek ve kaydet
    if len(contours) > 0:
        # Mavi cisimlerin etrafına yeşil dikdörtgen çiz
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.imwrite('blue_object_detected.jpg', frame)
        break
    
    # Ekranı göster
    cv2.imshow('frame', frame)
    
    # 'q' tuşuna basılana kadar beklemeye devam et
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizle ve kapat
cap.release()
cv2.destroyAllWindows()
