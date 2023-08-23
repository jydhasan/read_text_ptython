import cv2
import pytesseract
from pytesseract import Output

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path to your Tesseract installation

# Open the webcam (live video stream)
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale (Tesseract works better with grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform text detection using Tesseract OCR
    results = pytesseract.image_to_data(gray, output_type=Output.DICT)
    
    for i, text in enumerate(results['text']):
        if text:
            x, y, w, h = results['left'][i], results['top'][i], results['width'][i], results['height'][i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow('Text Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
