import os
import time
import pigpio

class UART():
	def __init__(self, tx_pin, baudrate) -> None:
		self.tx_pin = tx_pin
		self.baudrate = baudrate

		self.pi = pigpio.pi()

		while not self.pi.connected:
			print("trying to connect..")
			os.system("sudo pigpiod")
			time.sleep(1)
			self.pi = pigpio.pi()
			
		pigpio.exceptions = False
		self.pi.set_mode(self.tx_pin, pigpio.OUTPUT) 
		self.pi.serial_close(self.tx_pin)
		pigpio.exceptions = True

	def write(self, packet):
		self.send_command(packet)

	def send_command(self, packet):
		self.pi.wave_clear()
		self.pi.wave_add_serial(self.tx_pin, self.baudrate, packet, bb_bits=8)  
		wid = self.pi.wave_create()
		self.pi.wave_send_once(wid)  
		while self.pi.wave_tx_busy():  
			pass
		self.pi.wave_delete(wid)
