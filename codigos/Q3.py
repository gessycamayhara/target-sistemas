# Questão 3 do questionário da Target Sistemas

import json 

# Carrega os dados do arquivos JSON
with open('dados.json') as f:
    faturamento = json.load(f)
    
menor_faturamento = float('inf')
maior_faturamento = 0
dias_com_faturamento = 0
soma_faturamento = 0

for valor in faturamento.values():
    if valor > 0:
        dias_com_faturamento += 1
        soma_faturamento += valor
        menor_faturamento = min(menor_faturamento, valor)
        maior_faturamento = max(maior_faturamento, valor)
        
media_mensal = soma_faturamento / dias_com_faturamento

dias_acima_media = 0
for valor in faturamento.values():
    if valor > media_mensal:
        dias_acima_media += 1
        
print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")            