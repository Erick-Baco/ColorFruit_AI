
import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem1101', 9600)
time.sleep(2)

mensaje = arduino.readline()

print(mensaje)
arduino.close()


