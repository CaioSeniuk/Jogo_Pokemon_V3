import os, random, time
import pandas as pd

def introducao():
    os.system("cls")
    print('\n',('-'*30), "JOGO POKEMON",('-'*30))
    print(f"\nBem-vindo ao mundo de Pokémon!\n")
    print(f"\nMeu nome é Professor Carvalho.\nEste é um lugar especial, onde pessoas como você treinam para se tornar o Mestre Pokémon número 1 do mundo!")
    print(f"\nOs Pokémons são criaturas incríveis que compartilham o mundo com os seres humanos!\n")
    print(f"Atualmente, existem centenas de espécies de Pokémon documentadas.\n\nA sua incrível tarefa será capturar, treinar e lutar com todos eles.")
    time.sleep(4)

def pokemon_ganho(nome):
    os.system("cls")
    print(f"Olá, {nome}!\n\nSeja Bem-vindo.")
    print("\n\n--VOCÊ GANHOU UM POKÉMON DO DOUTOR CARVALHO--\n")
    dados = pd.read_csv("rattata.csv")
    print(dados)
    time.sleep(2)
    print("\nVeja sua Pokedéx para conferir os seus Pokémons...")
    pokedex.append("rattata")
    
def o_que_fazer():
    print("\nO que devemos fazer?\n\n1- Entrar na floresta\n2- Entrar na caverna\n3- Ver Pokedex\n4- Sair do Jogo")

def sorteio_pokemon_encontrado(pokemon):
    pokemon_sorteado = random.randint(0,len(pokemon)-1)
    return pokemon[pokemon_sorteado]

def tentativa_captura_floresta():
    tentativa = random.randint(0,99)
    if 0<=tentativa>=49: #50% de chance para CAPTURAR
        return 1
    else: #50% de chance para NÃO CAPTURAR
        return 2

def tentativa_captura_caverna():
    tentativa = random.randint(0,99)
    if 0<=tentativa>=34: #35% de chance para CAPTURAR
        return 1
    else: #65% de chance para NÃO CAPTURAR
        return 2

def atributos_tabela_floresta(pokemon_encontrado_floresta):
    if pokemon_encontrado_floresta == "Pikachu":
        dados = pd.read_csv("pikachu.csv")
        print(dados)
    elif pokemon_encontrado_floresta == "Golem":
        dados = pd.read_csv("golem.csv")
        print(dados)
    elif pokemon_encontrado_floresta == "Blastoide":
        dados = pd.read_csv("blastoide.csv")
        print(dados)

def atributos_tabela_caverna(pokemon_encontrado_caverna):
    if pokemon_encontrado_caverna == "Bulbassaur":
        dados = pd.read_csv("bulbasaur.csv")
        print(dados)
    elif pokemon_encontrado_caverna == "Golduck":
        dados = pd.read_csv("golduck.csv")
        print(dados)
    elif pokemon_encontrado_caverna == "Charizard":
        dados = pd.read_csv("charizard.csv")
        print(dados)

def sorteio_pokebola():
    tentativa = random.randint(0,99)
    if -1<tentativa< 10: #10% de chance para ACHAR uma pokebola
        return 1


#SE QUISER ADICIONAR MAIS POKEMONS NO JOGO -> mudar a lista dos pokemons nas linhas 59 e 60, mudar a qtd total de pokémons na linha 68 para reconhecer quando o jogador capturou todos os pokémons
#adicionar arquivo com tabela de atributos nas funções da linha 34 e 45 
pokedex = []
pokemons_floresta = ["Pikachu", "Golem", "Blastoide"]
pokemons_caverna = ["Bulbassaur", "Golduck", "Charizard"]
pokebolas = 3
introducao()
nome = input("\n\nQual o seu nome?\n-> ")
pokemon_ganho(nome)

while True:
    #O PROGRAMA ENCERRARÁ QUANDO O JOGADOR CAPTURAR TODOS OS POKÉMONS
    if len(pokedex) == 7:
        os.system("cls")
        print('\n',('-'*30), "FIM DE JOGO",('-'*30))
        print(f"\nParabéns, você capturou todos os pokémons!\n\n" + "\nPokedéx: {pokedex}")
        break

    #O PROGRAMA ENCERRARÁ SE AS POKEBOLAS ACABAREM
    if pokebolas == 0:
        print("\nAcabaram as tentativas...\n")
        break

    #O QUE DEVEMOS FAZER?
    print("\nO que devemos fazer?\n\n1- Entrar na floresta\n2- Entrar na caverna\n3- Ver Pokedéx\n4- Sair do Jogo")
    resposta_o_que_fazer = int(input("\n-> "))


    #ENTRAR NA FLORESTA
    if resposta_o_que_fazer == 1:  
        os.system("cls") 
        print('\n',('-'*30), "Escolheu entrar na Floresta",('-'*30))

        while True:

            #Sorteio para encontrar uma pokebola
            pokebola_adicional = sorteio_pokebola()
            if pokebola_adicional == 1:
                print("\n--VOCÊ ENCONTROU UMA POKEBOLA--")
                pokebolas += 1
                print(f"\n\nPokebolas Totais: {pokebolas}\n")
            

            #Sorteio para encontrar um pokémon aleatório
            pokemon_encontrado_floresta = sorteio_pokemon_encontrado(pokemons_floresta)
            print(f"\nVocê encontrou com o pokémon: {pokemon_encontrado_floresta}\n")


            #Imprimir tabela de atributos do pokémon encontrado
            atributos_tabela_floresta(pokemon_encontrado_floresta) # type: ignore
            
            #Condição para evitar capturar o mesmo pokémon
            if pokemon_encontrado_floresta in pokedex:
                print("\nVocê já tem este pókemon...")
                break

            
            opcao_capturar = int(input("\nDeseja tentar capturá-lo?\n1- Sim\n2- Não\n\n-> "))

            #Condições para escolher capturar o pokemon ou não
            #Condição abaixo para TENTAR capturar
            if opcao_capturar == 1:
                #Chamada da função para ocorrer a tentativa de captura
                captura = tentativa_captura_floresta()
                if captura == 1:
                    print(f"\nPókemon {pokemon_encontrado_floresta} CAPTURADO com sucesso...\n")
                    pokedex.append(pokemon_encontrado_floresta)
                    break
                elif captura == 2:
                    print(f"\nPókemon {pokemon_encontrado_floresta} NÃO capturado, tente novamente...")
                    pokebolas -= 1
                    print(f"\nPokebolas restantes: {pokebolas}")
                    break

            #Condição abaixo para NÃO tentar capturar
            elif opcao_capturar == 2:
                print("\nSaindo da Floresta...")
                break
            #Condição para evitar o "input" de opções inválidas
            else:
                print("\nErro, insira uma opção válida\n")
                continue


    #ENTRAR NA CAVERNA
    elif resposta_o_que_fazer == 2:
        os.system("cls")
        print('\n',('-'*30), "Escolheu entrar na Caverna",('-'*30))

        while True:

            #Sorteio para encontrar uma pokebola
            pokebola_adicional = sorteio_pokebola()
            if pokebola_adicional == 1:
                print("\n--VOCÊ ENCONTROU UMA POKEBOLA--")
                pokebolas += 1
                print(f"\n\nPokebolas Totais: {pokebolas}\n")


            #Sorteio para encontrar um pokémon aleatório
            pokemon_encontrado_caverna = sorteio_pokemon_encontrado(pokemons_caverna)
            print(f"\nVocê encontrou com o pokémon: {pokemon_encontrado_caverna}\n")
            

            #Imprimir tabela de atributos do pokémon encontrado
            atributos_tabela_caverna(pokemon_encontrado_caverna) # type: ignore
            
            #Condição para evitar capturar o mesmo pokémon
            if pokemon_encontrado_caverna in pokedex:
                print("\nVocê já tem este pókemon...")
                break

            
            opcao_capturar = int(input("\nDeseja tentar capturá-lo?\n1- Sim\n2- Não\n\n-> "))

            #Condições para escolher capturar o pokemon ou não
            #Condição abaixo para TENTAR capturar
            if opcao_capturar == 1:
                #Chamada da função para ocorrer a tentativa de captura
                captura = tentativa_captura_caverna()
                if captura == 1:
                    print(f"\nPókemon {pokemon_encontrado_caverna} CAPTURADO com sucesso...\n")
                    pokedex.append(pokemon_encontrado_caverna)
                    break
                elif captura == 2:
                    print(f"\nPókemon {pokemon_encontrado_caverna} NÃO capturado, tente novamente...")
                    pokebolas -= 1
                    print(f"\nPokebolas restantes: {pokebolas}")
                    break

            #Condição abaixo para NÃO tentar capturar
            elif opcao_capturar == 2:
                print("\nSaindo da Caverna...")
                break
            #Condição para evitar o "input" de opções inválidas
            else:
                print("\nErro, insira uma opção válida\n")
                continue


    #VER POKEDÉX          
    elif resposta_o_que_fazer == 3:
        os.system("cls") 
        print('\n',('-'*30), "Escolheu ver a Pokedéx",('-'*30))
        print("Pokedéx: ", pokedex)
        continue


    #SAIR DO JOGO
    elif resposta_o_que_fazer == 4:
        print("\n\nAté logo!\n")
        break


    #OPÇÃO INVÁLIDA
    else:
        os.system("cls")
        print("\nErro, Insira uma opção válida...")
        continue
