import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_cursos = pd.read_csv('analise2/df_cursos.csv')

cursos = df_cursos['Major'].unique()
print(cursos)

figura2 = plt.figure(figsize=(15,18))
figura2.suptitle('Impacto do uso de IA no tempo economizado (por curso)')

c = 1

for curso in cursos:
    plt.subplot(3,2,c)
    x = df_cursos.loc[df_cursos['Major']==curso,'Task_Frequency_Daily']
    y= df_cursos.loc[df_cursos['Major']==curso,'Time_Saved_Hours_Weekly']
    plt.plot(x,y,zorder=2,marker='o')
    plt.title(curso)
    plt.xlabel('Frequência de uso de IA')
    plt.ylabel('Tempo economizado\n(horas/semana)')
    plt.grid(alpha=0.3,zorder=0,linestyle='--')
    plt.xticks(range(1,11))
    plt.yticks(range(6,12))

    c += 1

plt.subplots_adjust(bottom=0.15,hspace=0.7,wspace=0.3)
plt.savefig('relacao_IA_tempo.png')
plt.show()
