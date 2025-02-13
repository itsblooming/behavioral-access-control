from pynput import keyboard, mouse

# Функция для обработки нажатия клавиш
def on_key_press(key):
    try:
        print(f"Key pressed: {key.char}")  # Символьные клавиши
    except AttributeError:
        print(f"Special key pressed: {key}")  # Специальные клавиши, например, Shift или Ctrl

# Функция для обработки отпускания клавиш
def on_key_release(key):
    print(f"Key released: {key}")
    if key == keyboard.Key.esc:  # Остановка программы по клавише Escape
        return False

# Функция для обработки кликов мыши
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        print(f"Mouse released at ({x}, {y}) with {button}")

# Функция для обработки движения мыши
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# Функция для обработки прокрутки мыши
def on_scroll(x, y, dx, dy):
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# Запуск слушателей клавиатуры и мыши
def main():
    # Слушатель клавиатуры
    keyboard_listener = keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release
    )
    keyboard_listener.start()

    # Слушатель мыши
    mouse_listener = mouse.Listener(
        on_click=on_click,
        on_move=on_move,
        on_scroll=on_scroll
    )
    mouse_listener.start()

    # Ожидание завершения
    keyboard_listener.join()
    mouse_listener.join()

if __name__ == "__main__":
    main()