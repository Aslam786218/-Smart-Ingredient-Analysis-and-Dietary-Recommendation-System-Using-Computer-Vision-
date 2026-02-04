import cv2
from pyzbar.pyzbar import decode

camera_index = 1  # iPhone camera

cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("❌ Unable to access iPhone camera.")
    exit()

print("📱 Using iPhone camera... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame")
        break

    # Show frame
    cv2.imshow('iPhone Scanner', frame)

    # Detect barcodes
    codes = decode(frame)
    for code in codes:
        barcode_data = code.data.decode('utf-8')
        print(f"✅ Detected Code: {barcode_data}")
        # Optional: draw rectangle
        pts = code.polygon
        pts = [(pt.x, pt.y) for pt in pts]
        pts.append(pts[0])
        for i in range(len(pts)-1):
            cv2.line(frame, pts[i], pts[i+1], (0,255,0), 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
