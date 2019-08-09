import time
import tkinter
from threading import Thread
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

key_enable_disable = KeyCode(char='r')
key_exit = KeyCode(char='e')
DELAY = 0.001

class MouseClicker(Thread):

    def __init__(self, delay, button):
        super(MouseClicker, self).__init__()
        self.delay = delay
        self.button = button
        self.clicker_running = False
        self.program_running = True

    def run(self):
        while self.program_running:
            while self.clicker_running:
                mouse.click(self.button)
                time.sleep(self.delay)

    def start_clicker(self):
        self.clicker_running = True
    
    def stop_clicker(self):
        self.clicker_running = False

    def exit_clicker(self):
        self.stop_clicker()
        self.program_running = False

if __name__ == '__main__':

    #window = tkinter.Tk()
    #window.title('Auto Clicker')
    #window.mainloop()

    mouse = Controller()
    clicker = MouseClicker(DELAY, Button.left)
    clicker.start()

def on_press(key):
    if key == key_enable_disable:
        clicker.stop_clicker() if clicker.clicker_running else clicker.start_clicker()
    elif key == key_exit:
        clicker.exit_clicker()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()