# AI.py

import sys
from dfplayer import SimpleDFPlayerMini
from time import sleep

def try_command(name, args):
    '''queries dfplayer.py for the method name and returns the method'''
    try:
        func = getattr(player, name)
        command = func(*map(int, args)) if args else func()
        print("Command is: " + name)
    except AttributeError:
        print(f"Command {name} not found, try to write 'next_track' to invoke def next_track in dfplayer.py")
        print("Only commands without parameters are supported")
        print("'exit' to close the program'")
        return

print("DFPlayer Mini Example")

player = SimpleDFPlayerMini(tx_pin=14)

if len(sys.argv) > 1:
    command_name = sys.argv[1]
    command_args = sys.argv[2:]
    try_command(command_name, command_args)
else:
    while True:
        userInput = input("Write command: ")  # kérdezd meg a felhasználótól a parancsot
        if userInput == "exit":
            player.reset()
            exit()
        # Az inputot szétválasztjuk a szóközök mentén, és a parancsot és a paramétereket külön változókban tároljuk
        parts = userInput.split()
        command_name = parts[0]
        command_args = parts[1:]  # Nem konvertáljuk az arg-okat, csak a hangerő és track_index esetében kell
        try_command(command_name, command_args)
