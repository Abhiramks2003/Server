import pyautogui
while True:
    # Get the current mouse position, state and scroll
    x, y = pyautogui.position()
    print((x,y))
    # is_left_pressed, is_middle_pressed, is_right_pressed = pyautogui.mouseDown()
    pyautogui.scroll(1)
