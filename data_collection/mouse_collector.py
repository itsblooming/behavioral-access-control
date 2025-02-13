import time
import csv
from pynput import mouse

class MouseCollector:
    def __init__(self, output_file="mouse_data.csv"):
        self.output_file = output_file
        self.mouse_events = []
        self.start_time = time.time()

    def on_move(self, x, y):
        timestamp = time.time() - self.start_time
        self.mouse_events.append(("move", x, y, timestamp, None))
        print(f"Mouse moved to ({x}, {y}) at {timestamp:.4f}")

    def on_click(self, x, y, button, pressed):
        timestamp = time.time() - self.start_time
        event_type = "click_pressed" if pressed else "click_released"
        self.mouse_events.append((event_type, x, y, timestamp, None))
        print(f"Mouse {event_type} at ({x}, {y}) with {button}")

    def on_scroll(self, x, y, dx, dy):
        timestamp = time.time() - self.start_time
        self.mouse_events.append(("scroll", x, y, timestamp, (dx, dy)))
        print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

    def save_to_csv(self):
        with open(self.output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Event Type", "X", "Y", "Timestamp", "Extra Info"])
            writer.writerows(self.mouse_events)
        print(f"[INFO] Data saved to {self.output_file}")

    def start_listener(self):
        with mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll
        ) as listener:
            listener.join()
        self.save_to_csv()

if __name__ == "__main__":
    collector = MouseCollector()
    collector.start_listener()
