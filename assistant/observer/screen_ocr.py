import mss
from PIL import Image
import pytesseract

def capture_screen_text():
    """
    Captures the full screen and returns the extracted text using OCR.
    """
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # Full screen
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        text = pytesseract.image_to_string(img)
        return text
