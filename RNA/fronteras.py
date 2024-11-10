import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv('../ARDUINO/datos_rgb.csv')

# Asignar los valores 1, 0, 0 a las primeras 200 filas en las columnas 'a1', 'a2', 'a3'
df.loc[199:399, ['a1', 'a2', 'a3']] = [1, 1, 0]

# Guardar los cambios en un nuevo archivo CSV o sobreescribir el archivo original
df.to_csv('../ARDUINO/datos_rgb.csv', index=False)
