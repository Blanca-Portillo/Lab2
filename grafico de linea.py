import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
archivo = "movie.csv"  # Asegúrate de que este sea el nombre correcto del archivo
df = pd.read_csv(archivo)

# Mostrar las primeras filas del DataFrame para verificar los datos
print(df.head())

# Convertir 'release_date' a tipo datetime y extraer el año
df['release_date'] = pd.to_datetime(df['release_date'])
df['Año'] = df['release_date'].dt.year

# Agrupar por año y calcular la media de 'popularity' y 'vote_average'
popularidad_por_año = df.groupby('Año')['popularity'].mean()
calificacion_por_año = df.groupby('Año')['vote_average'].mean()

# Crear el gráfico de líneas
plt.figure(figsize=(14, 7))  # Ajustar el tamaño del gráfico

# Gráfico de popularidad
plt.plot(popularidad_por_año.index, popularidad_por_año, 
         marker='o', linestyle='--', label='Popularidad Promedio', 
         color='lightcoral', markersize=8, linewidth=2)

# Gráfico de calificación
plt.plot(calificacion_por_año.index, calificacion_por_año, 
         marker='s', linestyle='-', label='Calificación Promedio', 
         color='lightblue', markersize=8, linewidth=2)

# Personalizar el gráfico
plt.title('Evolución de la Popularidad y Calificación Promedio de Películas a lo Largo de los Años', fontsize=16, fontweight='bold')
plt.xlabel('Año', fontsize=14)
plt.ylabel('Valor Promedio', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)  # Mostrar leyenda
plt.grid(True, linestyle='--', alpha=0.7)  # Cuadrícula con estilo

# Añadir anotaciones
for i in range(len(popularidad_por_año)):
    if i % 5 == 0:  # Anotar cada 5 años
        plt.annotate(f'{popularidad_por_año.values[i]:.2f}', 
                     (popularidad_por_año.index[i], popularidad_por_año.values[i]), 
                     textcoords="offset points", 
                     xytext=(0,10), 
                     ha='center', fontsize=9, color='darkred')

# Ajustar diseño
plt.tight_layout()
plt.show()
