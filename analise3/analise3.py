import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_uso = pd.read_csv('analise3/df_uso.csv')
#print(df_uso.columns)

ferramentas = df_uso['Primary_AI_Tool'].unique()
#print(ferramentas)

figura3 = plt.figure(figsize=(20,15))
plt.suptitle('Usos principais de cada ferramenta de IA')

c=1

for ferramenta in ferramentas:
    plt.subplot(2,3,c)
    plt.title(ferramenta)
    x = df_uso.loc[df_uso['Primary_AI_Tool']==ferramenta,'Main_Usage_Case']
    y= df_uso.loc[df_uso['Primary_AI_Tool']==ferramenta,'0']
    plt.bar(x,y,zorder=2,color=['purple','tab:blue','green','orange','red'])
    plt.xticks(rotation=45)
    plt.yticks([5,10,15,20,25])
    plt.grid(alpha=0.5,zorder=0,linestyle='--')
    plt.xlabel('Ferramenta')
    plt.ylabel('Quantidade de usos')

    c+=1

plt.subplots_adjust(bottom=0.23,hspace=0.9,wspace=0.3)
#plt.savefig('relacao_ferramenta_uso.png')
plt.show()
