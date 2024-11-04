import serial
import csv
import time

# Configuración del puerto serie
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Cambia el puerto según corresponda
time.sleep(2)  # Tiempo para que se establezca la conexión

# Nombre del archivo CSV
csv_filename = 'datos_rgb.csv'

# Abre el archivo en modo de escritura
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Red", "Green", "Blue"])

    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                rgb_values = data.split(',')
                writer.writerow(rgb_values)
                print(f"Datos guardados: {rgb_values}")
    except KeyboardInterrupt:
        print("Finalizando la captura de datos.")

# Cierra la conexión serie
ser.close()
