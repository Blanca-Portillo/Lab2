import pandas as pd
import matplotlib.pyplot as plt

#  archivo CSV
archivo = "student_performance.csv"  # Asegúrate de que este sea el nombre correcto del archivo
df = pd.read_csv(archivo)

# verificar los datos
print(df.head())

# Verificar los nombres de las columnas
print("Columnas disponibles en el DataFrame:", df.columns)

# Seleccionar los 10 estudiantes con mrendimiento
top_students = df.nlargest(10, 'FinalGrade')

# Crear el gráfico de líneas
plt.figure(figsize=(10, 5))
plt.plot(top_students['Name'], top_students['AttendanceRate'], marker='o')

# Configurar el gráfico
plt.title('Tasa de Asistencia de los 10 Estudiantes con Mejor Rendimiento')
plt.xlabel('Estudiantes')
plt.ylabel('Tasa de Asistencia (%)')
plt.xticks(rotation=45)  # Rotar nombres 
plt.grid()
plt.tight_layout()

# Mostrar el gráfico
plt.show()

#link del Dataset que usé
#https://www.kaggle.com/datasets/haseebindata/student-performance-predictions