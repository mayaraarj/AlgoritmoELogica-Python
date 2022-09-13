print("\033[1;43mDados das pesquisa TSE - 2022\033[m")
print("O eleitorado brasileiro em 2022 é 6,21% maior que o registrado em 2018. \n"
      "A informação é do Tribunal Superior Eleitoral (TSE), que divulgou estatísticas \n"
      "sobre os 156 milhões de cidadãos aptos a votar nas eleições deste ano, \n"
      "no dia 2 de outubro. Segundo o TSE, os eleitores brasileiros estão distribuídos\n"
      " em 5.570 cidades no Brasil e 181 no exterior.")

execucao = True

while execucao:

    print("\033[1;33mDentre as perguntas abaixo, escolha sua OPÇÃO de consulta (indicando o número: 1, 2 ou 3):\033[m ")
    print("[ 1 ] A porcentagem de eleitores que vivem no exterior sobre o total do eleitorado brasileiro. \n"
          "[ 2 ] Indicar o sexo com a maior quantidade de eleitores brasileiros.\n"
          "[ 3 ] Indicar o maior e o menor nível quanto a escolaridade.")
    pergunta = int(input("\033[1;33mDigite sua OPÇÃO de consulta:\033[m "))
    if pergunta == 1:
        print("\033[1;31m[ 1 ] A porcentagem de eleitores que vivem no exterior sobre o total do eleitorado brasileiro. \033[m")
        print("\033[1;96m 671,100 mil eleitores vivem no exterior que representa 0,45% do total de eleitores brasileiros.\033[m")
    elif pergunta == 2:
        print("\033[1;31m[ 2 ] Indicar o sexo com a maior quantidade de eleitores brasileiros.\033[m ")
        print("\033[1;96m O sexo com maior quantidade de eleitores brasileiro é o sexo FEMININO com cerca de 52,6% (82,4 milhões).\n"
              " Em quanto os homens representam cerca de 47,3% (74 milhões)\033[m")
    elif pergunta == 3:
        print("\033[1;31m[ 3 ] Indicar o maior e o menor nível quanto a escolaridade.\033[m")
        print("\033[1;96m  Maior nivel de escolaridade : \033[1;93mENSINO MÉDIO (41,2milhões de eleitores que representa 26,3%)\n"
              "  \033[1;96mMenor nivel de escolaridade :\033[1;93m ENSINO SUPERIOR (17,1 milhões de eleitores que representa 10,9%)\033[m")
    else:
        while pergunta!=1 and pergunta!=2 and pergunta!=3:
            pergunta=int(input("\033[1;96m Opção invalida! tente novamente.  \033[m"))
        if pergunta == 1:
            print("\033[1;31m[ 1 ] A porcentagem de eleitores que vivem no exterior sobre o total do eleitorado brasileiro. \033[m")
            print(
                "\033[1;96m 671,100 mil eleitores vivem no exterior que representa 0,45% do total de eleitores brasileiros.\033[m")
        elif pergunta == 2:
            print("\033[1;31m[ 2 ] Indicar o sexo com a maior quantidade de eleitores brasileiros. \033[m")
            print(
                "\033[1;96m O sexo com maior quantidade de eleitores brasileiro é o sexo FEMENIMO com cerca de 52,6% (82,4 milhões).\n"
                " Em quanto os homens representam cerca de 47,3% (74 milhões)\033[m")
        elif pergunta == 3:
            print("\033[1;31m[ 3 ] Indicar o maior e o menor nível quanto a escolaridade.\033[m")
            print(
                "\033[1;96m  Maior nivel de escolaridade : \033[1;93mENSINO MÉDIO (41,2milhões de eleitores que representa 26,3%)\n"
                "  \033[1;96mMenor nivel de escolaridade :\033[1;93m ENSINO SUPERIOR (17,1 milhões de eleitores que representa 10,9%)\033[m")
        opcao = str(input('\033[1;43m Deseja escolher outra opcao? [S/N] \033[m ')).upper().strip()

        if opcao!='S' and opcao!='N':
            print("\033[1;96m Opção invalida!!!\033[m")
            print('')
        elif opcao == 'N':
            execucao = False
            exit('\033[1;31m Obrigado por usar nosso programa. \033[m ')

    print('')
    opcao = str(input('\033[1;43m Deseja escolher outra opcao? [S/N] \033[m ')).upper().strip()
    if opcao != 'S' and opcao != 'N':
        print("\033[1;96m Opção invalida!!!\033[m")
        print('')
    elif opcao == 'N':
        execucao = False
        exit('\033[1;31m Obrigado por usar nosso programa. \033[m ')

    print("\033[1;31mTENTE NOVAMENTE!!!\033[m")

    #Equipe: Allyson Frank Ribeiro Calvet, Caíque Luís Figueiredo Teles de Menezes,Eduardo Silva Weba Ferreira, Elias lima da Silva Filho, Maria Fernanda Martins Mirabile, Mayara Araujo Abreu.
