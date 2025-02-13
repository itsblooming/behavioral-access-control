import time
import csv
from pynput import keyboard

class KeyboardCollector:
    def __init__(self, output_file="keyboard_data.csv"):
        self.output_file = output_file
        self.key_events = []
        self.start_time = time.time()
        self.last_press_time = None  # Для вычисления интервалов между нажатиями

    def on_key_press(self, key):
        timestamp = time.time() - self.start_time
        try:
            key_value = key.char
        except AttributeError:
            key_value = str(key)

        interval = None
        if self.last_press_time is not None:
            interval = timestamp - self.last_press_time  # Время между нажатиями
        self.last_press_time = timestamp

        self.key_events.append((key_value, timestamp, interval, "press"))
        print(f"Key pressed: {key_value}, Time: {timestamp:.4f}, Interval: {interval}")

    def on_key_release(self, key):
        timestamp = time.time() - self.start_time
        try:
            key_value = key.char
        except AttributeError:
            key_value = str(key)

        self.key_events.append((key_value, timestamp, None, "release"))
        print(f"Key released: {key_value}, Time: {timestamp:.4f}")

        if key == keyboard.Key.esc:  # Остановка при нажатии ESC
            print("[INFO] Stopping keyboard listener...")
            return False

    def save_to_csv(self):
        with open(self.output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Key", "Timestamp", "Interval", "Event Type"])
            writer.writerows(self.key_events)
        print(f"[INFO] Data saved to {self.output_file}")

    def start_listener(self):
        with keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        ) as listener:
            listener.join()
        self.save_to_csv()  # Сохранение после выхода из программы

if __name__ == "__main__":
    collector = KeyboardCollector()
    collector.start_listener()
