num1 = 0
num2 = 0
resultado = 0
operacao = ''

num1 = int(input("Digite o primeiro número: "))
operacao = (input("Digite a operação: "))
num2 = int(input("Digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        resultado = "Não é possível dividir por zero."
    else: 
        resultado = num1 / num2
else: 
    resultado = "Operação inválida." 

print(f"Resultado: {resultado}")