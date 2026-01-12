Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Simulação de Dados de Entrega (Pontos na região central da cidade) [cite: 67]
# Representação de latitude e longitude dos pedidos recebidos
... data = {
...     'id': range(1, 13),
...     'lat': [-23.5505, -23.5515, -23.5500, -23.5530, -23.5540, -23.5520, 
...             -23.5580, -23.5590, -23.5575, -23.5600, -23.5610, -23.5595],
...     'lon': [-46.6333, -46.6340, -46.6320, -46.6360, -46.6370, -46.6355, 
...             -46.6400, -46.6410, -46.6395, -46.6420, -46.6430, -46.6415]
... }
... df = pd.DataFrame(data)
... 
... # 2. Algoritmo de Clustering (K-Means) [cite: 73, 74, 88, 108]
... # Divide os pedidos em 3 zonas (para 3 entregadores diferentes)
... kmeans = KMeans(n_clusters=3, random_state=42)
... df['zona'] = kmeans.fit_predict(df[['lat', 'lon']])
... 
... # 3. Lógica de Otimização (Simulação de Pesos em Grafos para A*) [cite: 67, 68, 74]
... # O algoritmo A* usaria estas distâncias como heurística para encontrar o menor caminho
... def calcular_distancia(p1, p2):
...     return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
... 
... # 4. Visualização dos Resultados (Output Relevante para o GitHub) [cite: 109, 114]
... plt.figure(figsize=(10, 7))
... colors = ['red', 'blue', 'green']
... for zona in range(3):
...     cluster = df[df['zona'] == zona]
...     plt.scatter(cluster['lon'], cluster['lat'], c=colors[zona], label=f'Zona {zona+1}', s=100)
... 
... plt.title('Sabor Express - Otimização por Clustering (K-Means)')
... plt.xlabel('Longitude')
... plt.ylabel('Latitude')
... plt.legend()
... plt.grid(True)
... plt.savefig('docs/resultado_clusters.png') # Salva o output solicitado [cite: 114]
... plt.show()
... 
