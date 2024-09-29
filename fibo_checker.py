def is_fibonacci(num):
    # Função para verificar se o número pertence à sequência de Fibonacci
    # Fórmula: Um número é Fibonacci se (5*n^2 + 4) ou (5*n^2 - 4) for um quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Verifica se o número dado satisfaz uma das duas condições da fórmula
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

# Input: informe um número para verificar se ele está na sequência de Fibonacci
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função e retorna a mensagem adequada
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
