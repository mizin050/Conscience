import datetime

def log_event(app, text):
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] {app}: {text[:200]}")
