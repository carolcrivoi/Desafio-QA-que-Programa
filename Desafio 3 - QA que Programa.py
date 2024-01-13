'''frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso +=junto[letra]
if inverso == junto:
    print ("Temos um palíndromo!")
else:
    print ("A frase digitada não é um palíndromo!")'''

texto = input('Digite uma palavra ou frase: ')

texto_formatado = texto.replace(' ', "")
texto_formatado = texto_formatado.replace(',', "")
texto_formatado = texto_formatado.replace('.', "")
texto_formatado = texto_formatado.replace('!', "")
texto_formatado = texto_formatado.replace('?', "")
texto_formatado = texto_formatado.lower()

texto_invertido = ""

for caractere in texto_formatado:
    texto_invertido = caractere + texto_invertido

if texto_formatado== texto_invertido:
    resultado = "É um palíndromo."
else: resultado = "Não é um palíndromo."

print(resultado)