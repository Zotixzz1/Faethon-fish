from pynput.mouse import Controller, Button

_mouse = Controller()

def mouse_up():
    _mouse.press(Button.left)

def mouse_down():
    _mouse.release(Button.left)
