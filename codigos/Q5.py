# Questão 5 do questionário da Target Sistemas

palavra = input()
invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]
    
print(invertida)    