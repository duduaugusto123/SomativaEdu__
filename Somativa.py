import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


arquivo = "dados_motor.csv"
dados_original =  pd.read_csv(arquivo)
dados_dict = dados_original.to_dict("list")
dados_amostra = dados_original.iloc[10:24].to_dict("list")



print(dados_amostra)

vel_motor_ok = []
vel_motor_ruim = []
rotacao_motor = []


dados_amostra_presao_combu = dados_dict["Pressao Combustivel"][10:24]
dados_temp_arrefe = dados_dict["Temperatura Arrefecimento"][10:24]
condicao_motor = dados_dict["Condicao Motor"]

tamanho_amostra = len(dados_amostra_presao_combu)
print(dados_amostra_presao_combu)

for n in range(len(condicao_motor)):
    if dados_dict["Condicao Motor"][n] == 1:
        vel_motor_ok.append(dados_dict["Rotacao"][n])
    else:
        vel_motor_ruim.append(dados_dict["Rotacao"][n])
    rotacao_motor.append(dados_dict["Rotacao"][n])



print(vel_motor_ruim)
print(vel_motor_ok)

plt.subplot(1, 3, 1)
plt.hist(dados_amostra_presao_combu, bins='auto', alpha=0.7, rwidth=0.85)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma - Pressão Combustível')

plt.subplot(1, 3, 2)
plt.boxplot(dados_temp_arrefe)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Boxplot - Temperatura Arrefecimento')

q1 = np.percentile(dados_temp_arrefe, 25)
q2 = np.percentile(dados_temp_arrefe, 50)
q3 = np.percentile(dados_temp_arrefe, 75)
li = q1 - 1.5 * (q3 - q1)
ls = q3 + 1.5 * (q3 - q1)

plt.text(0.95, q1, f'Q1: {q1:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(0.95, q2, f'Q2: {q2:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(0.95, q3, f'Q3: {q3:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(0.95, li, f'LI: {li:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(0.95, ls, f'LS: {ls:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))


plt.subplot(1, 3, 3)
plt.hist(rotacao_motor, bins="auto", alpha=0.7, rwidth=0.85)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma - Rotação Motor')

media = np.mean(rotacao_motor)
desvio_padrao = np.std(rotacao_motor)
limite_inferior = media - desvio_padrao
limite_superior = media + desvio_padrao

print("Faixa de valores onde esperamos encontrar cerca de 68% dos valores:")
print("Limite Inferior:", limite_inferior)
print("Limite Superior:", limite_superior)

plt.axvline(limite_inferior, color='r', linestyle='--', label='Limite Inferior (68%)')
plt.axvline(limite_superior, color='g', linestyle='--', label='Limite Superior (68%)')
plt.legend()

fig, ax = plt.subplots()

ax.boxplot([vel_motor_ruim, vel_motor_ok], labels=['Velocidade Motor Ruim', 'Velocidade Motor OK'])
ax.set_xlabel('Condição do Motor')
ax.set_ylabel('Velocidade do Motor')
ax.set_title('Boxplot - Velocidade do Motor')


q1_ruim = np.percentile(vel_motor_ruim, 25)
q2_ruim = np.percentile(vel_motor_ruim, 50)
q3_ruim = np.percentile(vel_motor_ruim, 75)
li_ruim = q1_ruim - 1.5 * (q3_ruim - q1_ruim)
ls_ruim = q3_ruim + 1.5 * (q3_ruim - q1_ruim)

q1_ok = np.percentile(vel_motor_ok, 25)
q2_ok = np.percentile(vel_motor_ok, 50)
q3_ok = np.percentile(vel_motor_ok, 75)
li_ok = q1_ok - 1.5 * (q3_ok - q1_ok)
ls_ok = q3_ok + 1.5 * (q3_ok - q1_ok)

plt.text(1 + 0.25, q1_ruim, f'Q1 Ruim: {q1_ruim:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1+ 0.25, q2_ruim, f'Q2 Ruim: {q2_ruim:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1+ 0.25, q3_ruim, f'Q3 Ruim: {q3_ruim:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1+ 0.25, li_ruim, f'LI Ruim: {li_ruim:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1+ 0.25, ls_ruim, f'LS Ruim: {ls_ruim:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))

plt.text(2+ 0.25, q1_ok, f'Q1 OK: {q1_ok:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(2+ 0.25, q2_ok, f'Q2 OK: {q2_ok:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(2+ 0.25, q3_ok, f'Q3 OK: {q3_ok:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(2+ 0.25, li_ok, f'LI OK: {li_ok:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(2+ 0.25, ls_ok, f'LS OK: {ls_ok:.2f}', va='center', ha='right', bbox=dict(facecolor='white', edgecolor='black'))


plt.figure(figsize=(8, 6))

correlacao_matrix = dados_original.corr()


sns.heatmap(correlacao_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação de Pearson')

corelacao_da_rotacao = correlacao_matrix['Rotacao'].drop('Rotacao')
mais_afeta_rotacao = corelacao_da_rotacao.idxmax()
menos_afeta_rotacao = corelacao_da_rotacao.idxmin()

print("Variável que mais afeta a rotação do motor:", mais_afeta_rotacao)
print("Variável que menos afeta a rotação do motor:", menos_afeta_rotacao)

#Linearização
tamanho = len(dados_dict["Rotacao"])
contador = range (tamanho)
log_Rotacao= []
log_Pressao_O=[]
log_Pressao_C= []
log_Pressao_A= []
log_Temperatura_O=[]
log_Temperatura_A=[]
i = 0
dados_Rotacao = []
dados_Pressao_O= []
dados_Pressao_C= []
dados_Pressao_A= []
dados_Temperatura_O= []
dados_Temperatura_A= []
e = 0

for i in range(len(dados_dict['Amostra'])):
    if i != (2160-1) and i != (7585-1) and i != (8483-1) and i != (11050-1) and i != (17162-1):  #tirando as linhas q tem algum dado 0.00
        dados_Rotacao.append(dados_dict['Rotacao'][i])
        dados_Pressao_O.append(dados_dict['Pressao Oleo'][i])
        dados_Pressao_C.append(dados_dict['Pressao Combustivel'][i])
        dados_Pressao_A.append(dados_dict['Pressao Arrefecimento'][i])
        dados_Temperatura_O.append(dados_dict['Temperatura Oleo'][i])
        dados_Temperatura_A.append(dados_dict['Temperatura Arrefecimento'][i])
valor = 0

for e in range(len(dados_Rotacao)):
    valor = np.log(dados_Rotacao[e])
    log_Rotacao.append(valor)

    valor = np.log(dados_Pressao_O[e])
    log_Pressao_O.append(valor)

    valor = np.log(dados_Pressao_C[e])
    log_Pressao_C.append(valor)

    valor = np.log(dados_Pressao_A[e])
    log_Pressao_A.append(valor)

    valor = np.log(dados_Temperatura_O[e])
    log_Temperatura_O.append(valor)

    valor = np.log(dados_Temperatura_A[e])
    log_Temperatura_A.append(valor)


print(len(dados_dict['Pressao Oleo']))
matriz_corr=[log_Rotacao,log_Pressao_O,log_Pressao_A,log_Pressao_C,log_Pressao_A,log_Temperatura_O]
rho_linearizado = np.corrcoef(matriz_corr)

#Cálculo da correlação linear de Pearson
mapa_calor = sb.heatmap(rho_linearizado, annot=True)
plt.title("G)")



plt.tight_layout()
plt.show()
