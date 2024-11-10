import serial
import csv
import time

# Configuración del puerto serie
ser = serial.Serial('/dev/cu.usbmodem1201', 9600)  # Cambia el puerto según corresponda
time.sleep(2)  # Tiempo para que se establezca la conexión

# Nombre del archivo CSV
csv_filename = 'datos_rgb.csv'

# Abre el archivo en modo de escritura
with open(csv_filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["R", "G", "B", "a1", "a2", "a3"])
    seccion = ['1', '1', '0']
    num_datos = 0
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                rgb_values = data.split(',')
                writer.writerow(rgb_values + seccion)
                num_datos += 1
                print(f"{num_datos}.- Datos guardados: {rgb_values}")
    except KeyboardInterrupt:
        print("Finalizando la captura de datos.")

# Cierra la conexión serie
ser.close()
