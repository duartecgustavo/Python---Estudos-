# Desafio 77 - Aula 16 : Programa que tenha uma TUPLA com varias palavras. Depois deve mostrar:
# Para cada pavra quais são suas VOGAIS.

tupla = ('pao', 'bebe', 'carro', 'casa', 'buceta', 'livro')

for palavra in tupla:
    print(f'A palavra \033[31m{palavra.upper()}\033[m tem as vogais: ',end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end=' ')
        print('')
