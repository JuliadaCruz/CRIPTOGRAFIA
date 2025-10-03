def criptografar(texto, chave):
    alfabeto = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    encoded = ""
    for letra in texto:
        index = alfabeto.index(letra)
        encoded_index = (index + chave) % len(alfabeto)
        encoded += alfabeto[encoded_index]
    return encoded

def descriptografar(texto, chave):
    alfabeto = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    decoded = ""
    for letra in texto:
        index = alfabeto.index(letra)
        decoded_index = (index - chave) % len(alfabeto)
        decoded += alfabeto[decoded_index]
    return decoded

print("Algoritmo de Criptografia e Descriptografia")
chave = int(input("Digite a chave que vai ser usada para criptografar e descriptografar: "))
texto = input("Digite o texto que vai ser criptografado ou descriptografado: ")
ask = input("Digite C para criptografar ou D para descriptografar o texto: ").upper()

if ask == "C":
    texto_criptado = criptografar(texto, chave)
    print("Texto criptografado:", texto_criptado)
elif ask == "D":
    texto_descriptado = descriptografar(texto, chave)
    print("Texto descriptografado:", texto_descriptado)
else:
    print("Opção inválida.")
