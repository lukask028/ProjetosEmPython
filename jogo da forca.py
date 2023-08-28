# jogo da forca
import random 
import string 
#lista de palavras possiveis
lista_de_palavras = ['banana', 'repolho','tomate ','uva ', 'cenoura', 'beterraba']

#palavra escolhida


# funcao para pegar a palavra da lista, atraves do metodo random
def palavra_valida(lista_de_palavras):
    palavra = random.choice(lista_de_palavras)
    while '-' in palavra or ' ' in palavra: 
        palavra = random.choice(lista_de_palavras)
    
    return palavra.upper()

# funcao para o jogo da forca
def hangman():
    palavra = palavra_valida(lista_de_palavras)
    letra_palavra = set(palavra) # letra na palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() # letras usadas para adivinhar
    # qual letra atualmente usada
    print("Jogo da forca")
    
    while  len(letra_palavra) >= 0:  
        palavra_lista = [letra if letra in letras_usadas else '-' for letra in palavra]
        # letras usadas 
        print("Você usou essas letras: ", ' '.join(letras_usadas))
        # palavra escolhida
        print("palavra atual:", ' '.join(palavra_lista))
        
        if '-' not in palavra_lista:
            break
        # letra escolhida pelo usuario
        letra_usuario = input("Adivinhe uma letra:").upper()
       
    
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            
            if letra_usuario in letra_palavra:
                letra_palavra.remove(letra_usuario)
                print('')
            else:
                print(f"A letra, {letra_usuario}, não está na palavra.")
        elif letra_usuario in letras_usadas:
            print("Você já usou essa letra, tente outra!!")
        else:
            print("Caractere inválido")
      # chega aqui quando as letras das palavras forem igual a 0      
    
        
    print("parabens, você adivinhou a palavra!! 🎉✅✅")
if __name__ == '__main__':
    hangman()