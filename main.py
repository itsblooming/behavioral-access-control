import logging
from data_collection.keyboard_collector import KeyboardCollector
from data_collection.mouse_collector import MouseCollector

# Set up logging
logging.basicConfig(filename='system.log', level=logging.INFO)

def start_keyboard():
    collector = KeyboardCollector()
    collector.start()
    logging.info("Keyboard collector started.")

def start_mouse():
    collector = MouseCollector()
    collector.start()
    logging.info("Mouse collector started.")

if __name__ == "__main__":
    start_keyboard()
    start_mouse()