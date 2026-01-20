import json
from pathlib import Path

STATE_FILE = Path("control/recording_state.json")

def load_recording_state() -> bool:
    if not STATE_FILE.exists():
        return True  # default ON
    with open(STATE_FILE, "r") as f:
        return json.load(f).get("recording", True)

def set_recording_state(value: bool):
    STATE_FILE.parent.mkdir(exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump({"recording": value}, f)
