#Implemente um programa que leia, valide e analise dados informados pelo usuário.
#Os dados são meteorológicos e referem-se aos dados de 2021 (de janeiro a dezembro)
#registrados em uma cidade.

#Variáveis de controle, fiz elas para que o loop do programa principal só acabasse quando as 3 variáveis
#fossem verdadeiras "True", como isso acontece? Após o usuário preencher os meses 1, 6 e 12, o programa
#Enfim parte para a próxima fase de análise dos dados recebidos. Obviamente é um metodo situacional.
#Se o usuário dicidir preeencher os meses 1, 6 e 12 por primeiro o programa irá dar erro, pois às outras
#variáveis de temperatura não serão declaradas, decidi deixar o programa assim mesmo, pois tentando
#trabalhar apenas com os conhecimentos aprendidos da aula 1 até a aula 5. (terá apenas uma excessão):
informe1 = False
informe2 = False
informe3 = False

#Variáveis para capturar e análise dos dados vindo do usuário:
tempMedAnual = 0
mesesEscaldantes = 0
mesmaisQuente = 0
nomeMesmaisQuente = "Nome mês"
mesmaisfrio = 100
nomeMesmaisFrio = "Nome mês"

#Início visual do software:
print("INFORMAÇÕES SOBRE O PROGRAMA:")

#Loop central, usado para validar o primeiro input e controlar o programa para
#que só avance após todos os dados serem recebidos:
for repetir in range(1, 100):

    #Condição de continuação do loop principal, encerra somente com todos os informes = True:
    if informe1 == False or informe2 == False or informe3 == False:
        mes = input("\nInforme o mês e a temperatura máxima de TODOS os mêses do ano para receber uma análise climática."
                    "\n(sendo janeiro: 1, fevereiro: 2, março: 3...dezembro: 12): ")

        #Variável usada para validar o mês de entrada, evitando que o software quebre com str:
        validar1 = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"

        #Validação da entra:
        if mes in validar1:
            #Conversão de str para inteiro:
            mes = int(mes)

            #Aqui começa o processo de verificação de entrada, ao digitar o mês o if direciona ele para um for
            #Lá será validado a temperatura, verificação se o mês é mais quente ou frio, média de temperaturas
            # e verificação se é um mês escaldante:
            if mes == 1:
                #Usei um range até 100 para repetir, novamente é uma estimativa e esperasse que o usuário não erre
                #100 vezes. Caso contrário o programa iria quebrar, visto que ainda não aprendi sobre loops
                #indeterminados
                for repetir in range(1, 100):
                    #Aqui usei o try para validar a entrada caso fosse str, já tenho uma base em programação
                    #principalmente com Python, poderia encurtar várias partes do código, mas queria construir
                    #esse software usando apenas os conceitos que aprendi nas aulas, porém mesmo após várias
                    #tentativas não consegui e optei por usar o try/except.
                    try:
                        #Entrada de dados vindo do usuário:
                        tempmax1 = float(input("Digite a temperatura máxima de Janeiro: "))
                        #Verificando se está no intervalo válido da temperatura:
                        if tempmax1 < -60 or tempmax1 > 50:
                            #Caso não está no intervalo:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            #Caso esteja no intervalo:
                            #Variável de soma para cálculo da média:
                            tempMedAnual += tempmax1
                            #variável "informe" citado antes no inicio do programa para garantir que o usuário digite
                            #Todos os dados de cada mês:
                            informe1 = True
                            #Verificando se o mês é escaldante:
                            if tempmax1 > 33:
                                mesesEscaldantes += 1
                            #Procurando o mês mais quente, a verificação é feita com o último valor e o atual:
                            if tempmax1 > mesmaisQuente:
                                mesmaisQuente = tempmax1
                                #Variável usada para msotra o mês mais quente:
                                nomeMesmaisQuente = "Janeiro"
                            #Procurando o mês mais frio, a verificação é feita da mesma forte para o quente, porém
                            #A variável "mesmaisfrio" aqui começa com valor "100" sendo assim todas as verificações
                            #são feitas considerando que o próximo valor será menor. Caso usa-se uma variável de valor
                            #zero não seria possível fazer isso, pois foi o que considerei e conclusão que cheguei.
                            if tempmax1 < mesmaisfrio:
                                mesmaisfrio = tempmax1
                                nomeMesmaisFrio = "Janeiro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 2:
                for repetir in range(1, 100):
                    try:
                        tempmax2 = float(input("Digite a temperatura máxima de Fevereiro: "))
                        if tempmax2 < -60 or tempmax2 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax2
                            if tempmax2 > 33:
                                mesesEscaldantes += 1
                            if tempmax2 > mesmaisQuente:
                                mesmaisQuente = tempmax2
                                nomeMesmaisQuente = "Fevereiro"
                            if tempmax2 < mesmaisfrio:
                                mesmaisfrio = tempmax2
                                nomeMesmaisFrio = "Fevereiro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 3:
                for repetir in range(1, 100):
                    try:
                        tempmax3 = float(input("Digite a temperatura máxima de Março: "))
                        if tempmax3 < -60 or tempmax3 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax3
                            if tempmax3 > 33:
                                mesesEscaldantes += 1
                            if tempmax3 > mesmaisQuente:
                                mesmaisQuente = tempmax3
                                nomeMesmaisQuente = "Março"
                            if tempmax3 < mesmaisfrio:
                                mesmaisfrio = tempmax3
                                nomeMesmaisFrio = "Março"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 4:
                for repetir in range(1, 100):
                    try:
                        tempmax4 = float(input("Digite a temperatura máxima de Abril: "))
                        if tempmax4 < -60 or tempmax4 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax4
                            if tempmax4 > 33:
                                mesesEscaldantes += 1
                            if tempmax4 > mesmaisQuente:
                                mesmaisQuente = tempmax4
                                nomeMesmaisQuente = "Abril"
                            if tempmax4 < mesmaisfrio:
                                mesmaisfrio = tempmax4
                                nomeMesmaisFrio = "Abril"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 5:
                for repetir in range(1, 100):
                    try:
                        tempmax5 = float(input("Digite a temperatura máxima de Maio: "))
                        if tempmax5 < -60 or tempmax5 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax5
                            if tempmax5 > 33:
                                mesesEscaldantes += 1
                            if tempmax5 > mesmaisQuente:
                                mesmaisQuente = tempmax5
                                nomeMesmaisQuente = "Maio"
                            if tempmax5 < mesmaisfrio:
                                mesmaisfrio = tempmax5
                                nomeMesmaisFrio = "Março"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 6:
                for repetir in range(1, 100):
                    try:
                        tempmax6 = float(input("Digite a temperatura máxima de Junho: "))
                        if tempmax6 < -60 or tempmax6 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax6
                            informe3 = True
                            if tempmax6 > 33:
                                mesesEscaldantes += 1
                            if tempmax6 > mesmaisQuente:
                                mesmaisQuente = tempmax6
                                nomeMesmaisQuente = "Junho"
                            if tempmax6 < mesmaisfrio:
                                mesmaisfrio = tempmax6
                                nomeMesmaisFrio = "Junho"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 7:
                for repetir in range(1, 100):
                    try:
                        tempmax7 = float(input("Digite a temperatura máxima de Julho: "))
                        if tempmax7 < -60 or tempmax7 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax7
                            if tempmax7 > 33:
                                mesesEscaldantes += 1
                            if tempmax7 > mesmaisQuente:
                                mesmaisQuente = tempmax7
                                nomeMesmaisQuente = "Julho"
                            if tempmax7 < mesmaisfrio:
                                mesmaisfrio = tempmax7
                                nomeMesmaisFrio = "Julho"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 8:
                for repetir in range(1, 100):
                    try:
                        tempmax8 = float(input("Digite a temperatura máxima de Agosto: "))
                        if tempmax8 < -60 or tempmax8 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax8
                            if tempmax8 > 33:
                                mesesEscaldantes += 1
                            if tempmax8 > mesmaisQuente:
                                mesmaisQuente = tempmax8
                                nomeMesmaisQuente = "Agosto"
                            if tempmax8 < mesmaisfrio:
                                mesmaisfrio = tempmax8
                                nomeMesmaisFrio = "Agosto"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 9:
                for repetir in range(1, 100):
                    try:
                        tempmax9 = float(input("Digite a temperatura máxima de Setembro: "))
                        if tempmax9 < -60 or tempmax9 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax9
                            if tempmax9 > 33:
                                mesesEscaldantes += 1
                            if tempmax9 > mesmaisQuente:
                                mesmaisQuente = tempmax9
                                nomeMesmaisQuente = "Setembro"
                            if tempmax9 < mesmaisfrio:
                                mesmaisfrio = tempmax9
                                nomeMesmaisFrio = "Setembro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 10:
                for repetir in range(1, 100):
                    try:
                        tempmax10 = float(input("Digite a temperatura máxima de Outubro: "))
                        if tempmax10 < -60 or tempmax10 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax10
                            if tempmax10 > 33:
                                mesesEscaldantes += 1
                            if tempmax10 > mesmaisQuente:
                                mesmaisQuente = tempmax10
                                nomeMesmaisQuente = "Outubro"
                            if tempmax10 < mesmaisfrio:
                                mesmaisfrio = tempmax10
                                nomeMesmaisFrio = "Outubro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 11:
                for repetir in range(1, 100):
                    try:
                        tempmax11 = float(input("Digite a temperatura máxima de Novembro: "))
                        if tempmax11 < -60 or tempmax11 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax11
                            if tempmax11 > 33:
                                mesesEscaldantes += 1
                            if tempmax11 > mesmaisQuente:
                                mesmaisQuente = tempmax11
                                nomeMesmaisQuente = "Novembro"
                            if tempmax11 < mesmaisfrio:
                                mesmaisfrio = tempmax11
                                nomeMesmaisFrio = "Novembro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")
            #Mesmas verificações feitas no if:
            elif mes == 12:
                for repetir in range(1, 100):
                    try:
                        tempmax12 = float(input("Digite a temperatura máxima de Dezembro: "))
                        if tempmax12 < -60 or tempmax12 > 50:
                            print("Informe uma temperatura válida! (intervalo: -60º a 50º celsius)")
                        else:
                            tempMedAnual += tempmax12
                            informe2 = True
                            if tempmax12 > 33:
                                mesesEscaldantes += 1
                            if tempmax12 > mesmaisQuente:
                                mesmaisQuente = tempmax12
                                nomeMesmaisQuente = "Dezembro"
                            if tempmax12 < mesmaisfrio:
                                mesmaisfrio = tempmax12
                                nomeMesmaisFrio = "Dezembro"
                            break
                    except ValueError:
                        print("USE UMA ENTRADA VÁLIDA, APENAS NÚMEROS!")

        #Else da 1ª veirficação de entrada dos meses
        else:
            print("Valor inválido! Resumo: FORA DO INTERVALO OU VALOR NÃO É INTEIRO!")
    #Termino do loop após as variáveis informe passarem a ser True:
    else:
        print("\nA temperatura de todos os meses foi informada!")
        break

#Tabela de informações:
print("\nTABELA DE INFORMAÇÕES PARA ANÁLISE:")
#Temperaturas de todos os meses para facilitar o entendimento se o programa está ou não funcionando:
print(f"\nTemperatura máxima de cada mês:"
      f"\nJaneiro: {tempmax1}ºC"
      f"\nFevereiro: {tempmax2}ºC"
      f"\nMarço: {tempmax3}ºC"
      f"\nAbril: {tempmax4}ºC"
      f"\nMaio: {tempmax5}ºC"
      f"\nJunho: {tempmax6}ºC"
      f"\nJulho: {tempmax7}ºC"
      f"\nAgosto: {tempmax8}ºC"
      f"\nSetembro: {tempmax9}ºC"
      f"\nOutubro: {tempmax10}ºC"
      f"\nNovembro: {tempmax11}ºC"
      f"\nDezembro: {tempmax12}ºC")

#Cálculo da média das temperaturas anual:
print(f"\nMédia da temperatura máxima anual: {(tempMedAnual / 12):.1f}ºC")
#Meses escaldantes:
print(f"Quantidade de meses escaldantes(acima de 33ºC): {mesesEscaldantes}")
#Mês mais quente do ano:
print(f"Mês mais quente do ano: {nomeMesmaisQuente}, com temperatura de {mesmaisQuente}ºC")
#Mês mais frio(ou menos quente) do ano:
print(f"Mês menos quente do ano: {nomeMesmaisFrio}, com temperatura de {mesmaisfrio}ºC")

#Foi um programa desafiador de fazer, mesmo já feito alguns cursos de Python e ter uma base da linguagem
#e lógica de programação me peguei sendo surpreendido ao ter que estruturar um software voltado a um problema
#ou demanda real. Talvez tudo isso seja por minha conta mesmo, acabei não esboçando muita coisa no papel, nem
#fazendo um fluxograma para me ajudar a interpretar e entender melhor o que e como eu deveria fazer este
#software. Apesar de tudo me sinto gratificado, acredito ter chegado no resultado esperado para um iniciante
#Não tenho dúvida, havia uma maneira de diminuir o código ou deixam-lo mais limpo e organizado, ainda assim,
#Estou grato pelo desafio.
