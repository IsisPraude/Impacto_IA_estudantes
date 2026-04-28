import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df_confidence = pd.read_csv('analise1/df_confidence.csv')
df_maior_20 = df_confidence[df_confidence['Age']>=20]
df_menor_20 = df_confidence[df_confidence['Age']<20]
print(df_maior_20)
print(df_menor_20)


figura1 = plt.figure(figsize=(12,10))
figura1.suptitle('Relação entre uso de IA e confiança na carreira\ncom variação por idade')

# Gráfico para faixa de idade maior que 20 anos

plt.subplot(1,2,1)

x_jitter = df_maior_20['Task_Frequency_Daily'] + np.random.uniform(-0.2, 0.2, size=len(df_maior_20['Task_Frequency_Daily']))
y_jitter = df_maior_20['Career_Confidence_Score'] + np.random.uniform(-0.2, 0.2, size=len(df_maior_20['Career_Confidence_Score']))
plt.scatter(x_jitter,y_jitter,c=df_maior_20['GPA_Baseline'],cmap= 'viridis',s=40,alpha=0.5,edgecolors='black',linewidths=0.5)
plt.colorbar(label='GPA')
plt.xlabel('Frequência de uso')
plt.ylabel('Nível de confiança')
plt.xticks(range(1,11))
plt.yticks(range(1,11))
plt.grid(linestyle='--',alpha=0.3,zorder=0)
plt.title('Alunos com 20 anos ou mais')

coef = np.polyfit(df_maior_20['Task_Frequency_Daily'],df_maior_20['Career_Confidence_Score'], 1)
linha = np.poly1d(coef)

plt.plot(df_maior_20['Task_Frequency_Daily'], linha(df_maior_20['Task_Frequency_Daily']),linewidth=2,color='black')

# Gráfico para faixa de idade menor que 20 anos

plt.subplot(1,2,2)

x_jitter = df_menor_20['Task_Frequency_Daily'] + np.random.uniform(-0.2, 0.2, size=len(df_menor_20['Task_Frequency_Daily']))
y_jitter = df_menor_20['Career_Confidence_Score'] + np.random.uniform(-0.2, 0.2, size=len(df_menor_20['Career_Confidence_Score']))
plt.scatter(x_jitter,y_jitter,c=df_menor_20['GPA_Baseline'],cmap= 'viridis',s=40,alpha=0.5,edgecolors='black',linewidths=0.5)
plt.colorbar(label='GPA')
plt.xlabel('Frequência de uso')
plt.ylabel('Nível de confiança')
plt.xticks(range(1,11))
plt.yticks(range(1,11))
plt.grid(linestyle='--',alpha=0.3,zorder=0)
plt.title('Alunos com 20 anos ou menos')

coef = np.polyfit(df_menor_20['Task_Frequency_Daily'],df_menor_20['Career_Confidence_Score'], 1)
linha = np.poly1d(coef)

plt.plot(df_menor_20['Task_Frequency_Daily'], linha(df_menor_20['Task_Frequency_Daily']),linewidth=2,color='black')

plt.subplots_adjust(bottom=0.15)
plt.savefig('relacao_confianca_IA.png')
plt.show()