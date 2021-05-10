import pyfirmata
import time

board=pyfirmata.Arduino('COM3')
led=board.get_pin('d:13:o')

command=input()

while command!="out":
	if command=="on":
		
		led.write(1)
		time.sleep(1)
	elif command=="off":
		led.write(0)
		time.sleep(1)

	command=input()

		

	

	