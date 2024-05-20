import pygetwindow as gw
from pynput.mouse import Listener, Button, Controller

mouse = Controller()


def is_minecraft_running():
    windows = gw.getWindowsWithTitle("All of Create")
    return len(windows) > 0


if is_minecraft_running():
    is_button_held = False
    print('is minecraft running')
    def on_click(x, y, button, pressed):
        global is_button_held
        
        if button == Button.x2 and pressed:
            if is_button_held:
                #si el boton '4' es presionado y el clic izquierdo esta siendo sostenido, soltarlo
                mouse.release(Button.left)
                is_button_held = False
                print('Clic izquierdo liberado')
            else:
                #si el boton es presionado y el clic izquierdo no esta siendo sostenido, mantenerlo
                mouse.press(Button.left)
                is_button_held = True
                print('Click izquierdo presionado')
    with Listener(on_click=on_click) as listener:
        listener.join()
else:
    print('Minecraft no se esta ejecutando')