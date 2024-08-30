# Questão 2 do questionário da Target Sistemas

def encontrar_fibonacci(numero):
    
    fib_a = 0
    fib_b = 1
    
    while fib_b <= numero:
        if fib_b == numero:
            return True
        fib_a, fib_b = fib_b, fib_a + fib_b
    return False

numero = int(input("Digite um número: "))

if encontrar_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")    
    