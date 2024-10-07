import pandas as pd 
import matplotlib.pyplot as plt 

#archivo csv
archivo = "NominadosBalonDeOro.csv" #aseguranos de poner bien el archivo
df = pd.read_csv(archivo)

print(df.head()) #verifica datos

grouped_data = df.groupby('player')['Playing Time-90s'].sum()# Agrupar por jugador y sumar las nominaciones

#creamos el grafico 
plt.figure(figsize=(10, 8))  
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Nominaciones al Balón de Oro 2024')
plt.axis('equal')# Para que el gráfico sea un círculo

#mostrar
plt.show()

#link del dataset que use
#https://www.kaggle.com/datasets/farzammanafzadeh/ballon-dor-2024-nominees-league-stats

#el gráfico circular nos proporciona una visión clara y rápida de quiénes han sido los jugadores más 
#influyentes en las nominaciones al Balón de Oro. Permite ver tanto las figuras dominantes como la diversidad de 
#talento en la competición, y ayuda a identificar si hay una concentración de nominaciones en ciertos jugadores o si está más distribuida.
