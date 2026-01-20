import mss
import pytesseract
from PIL import Image

def capture_screen_text():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

        img = Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )

        text = pytesseract.image_to_string(img)
        return text
