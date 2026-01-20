import time
import logging

from observer.screen_capture import capture_screen_text
from control.state import load_recording_state
from memory.logger import log_event

logging.basicConfig(
    filename="logs/assistant.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

def main():
    logging.info("Assistant started")

    while True:
        recording = load_recording_state()

        if recording:
            try:
                text = capture_screen_text()
                if text.strip():
                    log_event("screen", text)
                    logging.info("Screen captured")
            except Exception as e:
                logging.error(f"Capture error: {e}")

        time.sleep(5)

if __name__ == "__main__":
    main()
