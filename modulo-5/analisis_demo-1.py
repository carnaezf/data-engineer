# Importamos la biblioteca Pandas, esencial para trabajar con datos tabulares
import pandas as pd

# Cargamos el archivo CSV con datos simulados de clientes
df = pd.read_csv("clientes_calidad_demo.csv")

# Mostramos las primeras 9 filas del DataFrame original para tener una vista inicial del contenido
print(df.head(9))

# ----------------------------------------

# Creamos una copia del DataFrame original
# Esto nos permite trabajar con libertad sin modificar los datos originales
df_copia = df.copy()

# Validamos si el campo 'email' tiene un formato válido
# La expresión regular verifica que haya caracteres antes y después del '@', y al menos un '.' después
df_copia['email_valido'] = df_copia['email'].str.contains(r'^\S+@\S+\.\S+$', na=False)

# Separador visual para organizar la salida en consola
print("------")

# Mostramos nuevamente las primeras 9 filas, ahora con la columna 'email_valido' agregada
print(df_copia.head(9))

# ----------------------------------------

print("------")

# Calculamos el porcentaje de valores no nulos por columna (completitud)
# Esto permite detectar campos incompletos en el dataset
completitud = df.notnull().mean() * 100
print(completitud)

# ----------------------------------------

print("------")

# Contamos cuántos registros están duplicados en el DataFrame original
# Es una forma de evaluar la unicidad del dataset
duplicados = df.duplicated().sum()
print(f"Duplicados detectados: {duplicados}")

# ----------------------------------------

print("------")

# Validamos si los valores de 'prioridad' están dentro del rango esperado (1 a 10)
# Se agrega una nueva columna que contiene True o False según corresponda
df_copia['prioridad_valida'] = df_copia['prioridad'].between(1, 10)

# Mostramos el DataFrame completo (con las nuevas columnas de validación)
print(df_copia)

# ----------------------------------------

print("------")

# Contamos cuántos valores son válidos y cuántos no en la columna 'prioridad_valida'
# Esto nos permite saber cuántas filas cumplen con el criterio de rango definido
print(df_copia['prioridad_valida'].value_counts())
