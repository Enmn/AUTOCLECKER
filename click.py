import time
import os
import sys
import threading
import ctypes

try:
    from yachalk import chalk
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Listener, Key
except ImportError:
    os.system("pip install yachalk")
    os.system("pip install pynput")






delay = 0.001
button = Button.left
start_stop_key = Key.f2
exit_key =  Key.f3

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW('AUTOCLICKER | Free version | V 1.0 | Coded by WHITE71wolf')
print("Running the tool...")
time.sleep(3)
os.system("cls")
print("Press on F2 to turn on autoclick\nand if you want to exit the tool, press on F3\n")

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True


    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        sys.stdout.write('\r' + f"STATUS : {chalk.green('ON ')}")
        sys.stdout.flush()
        if click_thread.running:
            click_thread.stop_clicking()
            sys.stdout.write('\r' + f"STATUS : {chalk.yellow('OFF')}")
            sys.stdout.flush()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        sys.stdout.write('\r' + f"STATUS : {chalk.red('Exiting the tool...')}")
        sys.stdout.flush()
        time.sleep(1)
        os.system('cls')


with Listener(on_press=on_press) as listener:
    listener.join()