### Printer Sound System
(for Klipper printers)
  this is a small program that can be used to add sound to printing events.


### Installing 
first we access the machine via ssh.
````
sudo apt-get update && apt-get upgrade
sudo apt install pigpio
sudo apt-get install python-pigpio python3-pigpio
````
then download the files to the printer
````
cd ~ && git clone https://github.com/Tompudex/Printer-Sound-System
cd Printer-Sound-System
chmod +x AI.sh
chmod +x AI.py
````
then, if it hasn't been there yet, install the [Shell-Gcode-Command](https://github.com/dw-0/kiauh/blob/095823bf288029a2d8e147c275b0c3b8549edd57/docs/gcode_shell_command.md#L1) add-on with [Kiauh](https://github.com/dw-0/kiauh/tree/master)

In the Kiauh menu, 4 (advance) and then 8 (extras)

### Using a macro
shell-gconde-command created a file when installing. the shell_command.cfg file
its content is an example that can be deleted.

this is the pause macro, for example
````

[gcode_shell_command Pause_sound]
command: 
        /home/pi/printer-sound-system/./AI.sh sel_track 1

timeout: 1.
verbose: False
[gcode_macro Pause_sound]
gcode:
    RUN_SHELL_COMMAND CMD=Pause_sound
````
the file that executes the task is a
  It is located in  `/home/pi/printer-sound-system/./AI.sh `.
  we use switches for this.  `sel_track (number) ` plays a selected file.

macro that can be used towards Klipper:
````
[gcode_macro Pause_sound] 
 gcode:
    RUN_SHELL_COMMAND CMD=Pause_sound
````
#### Extras

in addition to playback, we can also adjust volume and EQ

here all we have to do is use another switch, for example:  `set_vol (number) ` or  `set_eq (number) `.
you can find all available switches [here](https://github.com/thokis/SimpleDFPlayerMini-for-MicroPython/wiki/API)

#### Hardwer 
first you need a  DFPlayer Mini MP3 Player and an sd card. name the desired audio files on the sd card so that they are always 0001.mp3 0002.mp3 0003.mp3 etc.

### Serial
Serial communication must be enabled on the raspberry pi. for this we need the command ````sudo raspi-config````.
select the Interfacing options and the serial. 
## Connection

Basically you only have to connect the `RX` of the DFPlayerMini to the specific `TX` port of your board. Continuing our example from before `RX` from the DFPlayerMini goes to `GPI14` on the Raspberry Pi.
Also solder a 1k resistor inbetween the connection or professionally speaking in serial.
````
            |----DFPLAYER-MINI----|
PI 3.3v ----|VCC--------------BUSY|
PI GPIO14 --|RX---------------USB-|
            |TX---------------USB+|
            |DAC_R---------ADKEY_2|
            |DAC_I---------ADKEY_1|
      |-----|SPK_1------------IO_2|
   Speaker  |GND---------------GND|--- PI GND
      |-----|SPK_2------------IO_1|
            |--------|_SD_|-------|
````

No other Pins (except VCC and GND) should be used.


### this project is based on [Andreas'](https://github.com/andreaswatch) [SimpleDFPlayerMini-for-RaspberryPi](https://github.com/andreaswatch/SimpleDFPlayerMini-for-RaspberryPi) project.
