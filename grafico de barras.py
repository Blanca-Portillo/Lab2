import pandas as pd
import matplotlib.pyplot as plt  

#  archivo CSV
archivo = "spotify_data.csv"
df = pd.read_csv(archivo)


# Convertir los Streams a un tipo numérico solamente si  es necesario
df['Streams'] = pd.to_numeric(df['Streams'], errors='coerce')

# las 10 canciones más sonadas
top_canciones = df.nlargest(10, 'Streams')

# Creamos el gráfico de barras
plt.figure(figsize=(12, 8))
plt.barh(top_canciones['Songs & Artist'], top_canciones['Streams'], color='red')
plt.xlabel('Número de Streams')
plt.title('Top 10 Canciones Más Sonadas')
plt.gca().invert_yaxis()  # Invertimos el eje para que la canción más sonada esté en la parte de arriba
plt.show()
 
#LINK DEL DATASET QUE USÉ 
 #https://www.kaggle.com/datasets/asmonline/spotify-song-performance-dataset