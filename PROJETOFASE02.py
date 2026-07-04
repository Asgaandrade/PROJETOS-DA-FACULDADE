#FASE 02 DO PROJETO DA DISCIPLINA DE LÓGICA E PROGRAMAÇÃO:

#ENUNCIADO SIMPLIFICADO: Novamente vamos trabalhar com dados meteorológicos, mas agora os dados serão
#de um arquivo texto.  Nesta fase, você trabalhará com um conjunto de dados¹ (formato csv² em anexo
#disponibilizado no Material Complementar) contendo informações climáticas diárias do município
#brasileiro de Porto Alegre, entre os anos 1961 e 2016. O arquivo contém 18.564 registros com os
#campos: data, precipitação (volume de chuva em milímetros por m2), temperatura máxima (em graus
#celsius), temperatura mínima (em graus celsius), umidade relativa do ar (% entre 0 e 100) e a velocidade
#do vento (em m/s).

#Seu programa deve ser capaz de realizar:
#• Carga e preparação de dados: trabalhar com arquivos de dados, realizando a sua leitura, filtragem das
#informações relevantes e armazenamento em estruturas de dados adequadas para consulta.
#• Análise e visualização de dados: análises estatísticas diversas sobre os dados armazenados, por meio da
#implementação de algoritmos e geração de gráficos para a visualização dos resultados.

#===============================================================================================================

#INICIO DO PROJETO:

import matplotlib.pyplot as plt

listaDadosClimaticos = [] #LISTA QUE VAI RECEBER OS DADOS CLIMATICOS DO ARQUIVO.

#===============================================================================================================

#ABERTURA E LEITURA DO ARQUIVO .CSV:
with (open ("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv") as dadosClimaticos):
    dadosClimaticos.readline()
    for linhas in dadosClimaticos: #PASSANDO POR CADA LINHA DO ARQUIVO CSV.
        dadoClima = linhas[:-1].split(",")
        #CRIANDO UM DICIONÁRIO DE CADA LINHA DO ARQUIVO .CSV E ATRIBUINDO CADA VALOR A UMA CHAVE:
        dicionarioDadosClimaticos = {"DATA": dadoClima[0],
                                     "PRECIPITAÇÃO": float(dadoClima[1]),
                                     "TEMPMAXIMA": float(dadoClima[2]),
                                     "TEMPMINIMA": float(dadoClima[3]),
                                     "UMIDADE%": float(dadoClima[6]),
                                     "VELVENTO": float(dadoClima[7])}
        #ADICIONANDO CADA DICIONÁRIO A LISTA DE DADOS CLIMÁTICOS:
        listaDadosClimaticos.append(dicionarioDadosClimaticos)

#===============================================================================================================

#FUNÇÃO DE VALIDAÇÃO DE ENTRADA, DESENVOLVIDA PARA VALIDAR ENTRADA DO PERÍODO QUE O USUÁRIO DESEJA VER:
def validar(mes, ano):
    if mes.isnumeric():
        mes = int(mes)
        if mes in range(1, 13):
            if ano.isnumeric():
                ano = int(ano)
                if ano < 1961 or ano > 2016:
                    return False
                else: return True
            else: return False
        else: return False
    else: return False

#===============================================================================================================

#FUNÇÃO DE ESCOLHA DO USUÁRIO PARA VISUALIZAR DADOS DO SISTEMA, APÓS ESCOLHA DE PERÍODO:
def escolhaDados():
    valida = ["1", "2", "3", "4"]
    print("\n|MENU DE SELEÇÃO| - (INTERVALO SELECIONADO)")
    print("1 - VER TODOS OS DADOS\n"
        "2 - PRECIPITAÇÃO DE CHUVA\n"
        "3 - TEMPERATURA\n"
        "4 - UMIDADE E VELOCIDADE DO VENTO")
    escolhaUsuario = input("\nDIGITE SUA ESCOLHA: ")
    while escolhaUsuario not in valida:
        escolhaUsuario = input("> DIGITE SUA ESCOLHA: ")
    return escolhaUsuario

#===============================================================================================================

#FUNÇÃO DE VISUALIZAR OS DADOS:
def visualizarDados(mesIn, anoIn, mesFi, anoFi):

    #TRANSFORMANDO AS VARIÁVEIS EM INTEIRO:
    m_inicial = int(mesIn)
    a_inicial = int(anoIn)
    m_final = int(mesFi)
    a_final = int(anoFi)

    #TROCA DE DATA INICIAL E FINAL, CASO DATA FINAL MENOR QUE DATA INICIAL:
    if a_final < a_inicial:
        aux = a_inicial
        a_inicial = a_final
        a_final = aux
        aux = m_inicial
        m_inicial = m_final
        m_final = aux

    #CÁLCULO DE SCORE DE ANO/MES:
    score_inicial = (a_inicial * 12) + m_inicial
    score_final = (a_final * 12) + m_final

    #MENU DE ESCOLHA:
    escolhaUsu = escolhaDados()

    #CABEÇALHO COM BASE NA ESCOLHA DO USUÁRIO:
    if escolhaUsu == "1":
        print(f"\n{'DATA':<12} | {'CHUVA (mm)':<10} | {'T. MÁX (°C)':<11} | {'T. MÍN (°C)':<11} | {'UMIDADE (%)':<11} | {'VENTO (m/s)':<11}")
    elif escolhaUsu == "2":
        print(f"\n{'DATA':<12} | {'PRECIPITAÇÃO (mm)':<15}")
    elif escolhaUsu == "3":
        print(f"\n{'DATA':<12} | {'T. MÁX (°C)':<11} | {'T. MÍN (°C)':<11}")
    elif escolhaUsu == "4":
        print(f"\n{'DATA':<12} | {'UMIDADE (%)':<11} | {'VENTO (m/s)':<11}")

    #PONTO MAIS DIFICIL DO PROGRAMA, ENCONTRAR UMA MANEIRA DE PERCORER A LISTA DE DADOS CONFORME O MÊS E ANO
    #INICIAL ATÉ O MÊS E ANO FINAL, USEI UMA FÓRMULA MATEMÁTICA PARA GERAR UM SCORE PARA CADA DATA:
    for linha in listaDadosClimaticos:

        #SEPARANDO A DATA E PEGANDO MÊS E ANO:
        partes_data = linha["DATA"].split("/")
        mes_linha = int(partes_data[1])
        ano_linha = int(partes_data[2])

        #CÁLCULO DA LINHA ATUAL:
        score_linha = (ano_linha * 12) + mes_linha

        #VERIFICANDO SE A LINHA ESTÁ DENTRO DO PERÍODO SELECIONADO:
        if score_inicial <= score_linha <= score_final:

            #FILTRAGEM DO QUE EXIBIR COM BASE NA ESCOLHA DO USUÁRIO:
            if escolhaUsu == "1":
                print(
                    f"{linha['DATA']:<12} | {linha['PRECIPITAÇÃO']:<10.1f} | {linha['TEMPMAXIMA']:<11.1f} | {linha['TEMPMINIMA']:<11.1f} | {linha['UMIDADE%']:<11.1f} | {linha['VELVENTO']:<11.1f}")

            elif escolhaUsu == "2":
                print(f"{linha['DATA']:<12} | {linha['PRECIPITAÇÃO']:<15.1f}")

            elif escolhaUsu == "3":
                print(f"{linha['DATA']:<12} | {linha['TEMPMAXIMA']:<11.1f} | {linha['TEMPMINIMA']:<11.1f}")

            elif escolhaUsu == "4":
                print(f"{linha['DATA']:<12} | {linha['UMIDADE%']:<11.1f} | {linha['VELVENTO']:<11.1f}")


#===============================================================================================================

#FUNÇÃO QUE RECEBE A ENTRADA DE DADOS VINDO DO USUARIO, TEM COMO FUNÇÃO RECEBER O
#PERÍODO QUE O USUARIO DESEJA VISUALIZAR:
def periododoUsuario():
    #MENU EXPLICATIVO:
    print("\nVISUALIZAÇÃO DE INTERVALO DOS DADOS CLIMÁTICOS (1961 - 2016)")

    #LAÇO FEITO PARA CONTROLAR O MENU PRINCIPAL E AS ESCOLHAS DO USUÁRIO, USO DO WHILE, POIS É UM LAÇO
    #INDETERMINADO, NÃO SE SABE QUANTAS VESES O USUÁRIO PODE INFORMAR UMA ENTRADA INVÁLIDA:
    fechar_menu_inicial = True
    while fechar_menu_inicial:
        print("Para visualizar um intervalo de dados, você deve informar: Mês e Ano inicial / Mês e Ano final")
        escolha = input("Deseja visualizar um intervalo de dados especifico? [Sim/Não]: ").upper()
        #VALIDAÇÃO SE O USUÁRIO DESEJA OU NÃO VISUALIZAR UM INTERVALO DE DADOS:

        #SIM - PEDE O INTERVALO DESEJADO:
        if escolha == "SIM":
            print("\nINTERVALO DE DADOS VÁLIDO: \nMÊS: 1 - 12\nANO: 1961 - 2016")

            #PERÍODO INICIAL:
            mesInicial = input("MÊS INICIAL: ")
            anoInicial = input("ANO INICIAL: ")
            #VALIDAÇÃO DE ENTRADA, TANTO STRING QUANTO NÚMEROS FORA DO INTERVALO:
            while validar(mesInicial, anoInicial) == False:
                print("> ENTRADA INVÁLIDA: MÊS OU ANO FORA DE INTERVALO <")
                mesInicial = input("MÊS INICIAL: ")
                anoInicial = input("ANO INICIAL: ")


            #PERÍODO FINAL:
            mesFinal = input("MÊS FINAL: ")
            anoFinal = input("ANO FINAL: ")
            #VALIDAÇÃO DE ENTRADA, TANTO STRING QUANTO NÚMEROS FORA DO INTERVALO:
            while validar(mesFinal, anoFinal) == False:
                print("> ENTRADA INVÁLIDA: MÊS OU ANO FORA DE INTERVALO <")
                mesFinal = input("MÊS FINAL: ")
                anoFinal = input("ANO FINAL: ")

            #ESCOLHA E VISUALIZAÇÃO DOS DADOS ESCOLHIDOS:
            visualizarDados(mesInicial, anoInicial, mesFinal, anoFinal)

            fechar_menu_inicial = False

        #NÃO - ENCERRA O MENU INICIAL E SEGUE PARA PRÓXIMA PARTE DO PROGRAMA:
        elif escolha == "NÃO" or escolha == "NAO":
            print("\nPROGRAMA SEGUINDO PARA EXIBIÇÃO DOS DADOS PADRÕES DO SISTEMA:")
            break

        #VALIDAÇÃO DE ENTRADA:
        else:
            print("> A ENTRADA NÃO É VÁLIDA! DIGITE UM ENTRADA VÁLIDA: SIM/NÃO <\n")

#===============================================================================================================

#FUNÇÃO PARA ENCONTRAR E MOSTRAR O MÊS MAIS CHUVOSO DO INTERVALO DE DADOS:
def mesChuvoso():
    dicMesAno = {}

    for linhas in listaDadosClimaticos:
        precipita = linhas["PRECIPITAÇÃO"]
        datas = linhas["DATA"].split("/")
        mes = datas[1]
        ano = datas[2]
        mes_ano = mes +"/"+ ano #CHAVE DO DICIONÁRIO MES/ANO

        #SE CHAVE JÁ EXISTENTE, A PRECIPITAÇÃO É SOMA A SUA CHAVE CORRESPONDENTE:
        if mes_ano in dicMesAno:
            dicMesAno[mes_ano] += precipita
        #SE A CHAVE NÃO EXISTE ELA É CRIADA COM A CHUVA DO DIA:
        else:
            dicMesAno[mes_ano] = precipita

    #ENCONTRAR O MÊS/ANO MAIS CHUVOSO:
    maior_precipitacao = -1.0
    mes_mais_chuvoso = ""

    #PROCURANDO NO DICMESANO PARA VERIFICAR O MÊS/ANO MAIS CHUVOSO:
    for mes_ano, total_chuva in dicMesAno.items():
        if total_chuva > maior_precipitacao:
            maior_precipitacao = total_chuva
            mes_mais_chuvoso = mes_ano

    print("\nANÁLISE DE PRECIPITAÇÃO MÁXIMA")
    print(f"O mês/ano mais chuvoso registrado foi: {mes_mais_chuvoso}")
    print(f"Volume total de chuva no mês: {maior_precipitacao:.2f} mm")

#===============================================================================================================

#FUNÇÃO PARA CALCULAR A MÉDIA DA TEMPERATURA MÍNIMA DOS ÚLTIMOS 11 ANOS (2006-2016)
def mediaTempMinima():
    #LISTA COM O NOME DE CADA MÊS:
    nomes_meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                   "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    print("\nMÉDIA DA TEMPERATURA MÍNIMA DOS ÚLTIMOS 11 ANOS (2006-2016)")

    #VALIDAÇÃO DA ENTRADA DO USUÁRIO:
    mes_usuario = input("Digite o número do mês que deseja analisar (1 a 12): ")
    while not (mes_usuario.isnumeric() and 1 <= int(mes_usuario) <= 12):
        print("> ENTRADA INVÁLIDA! O mês deve ser um número entre 1 e 12. <")
        mes_usuario = input("Digite o número do mês (1 a 12): ")

    mes_analise = int(mes_usuario)
    nome_mes_extenso = nomes_meses[mes_analise]

    #DICIONÁRIOS AUXILIARES:
    dicSomas = {}  #GUARDA A SOMA DA TEMPERATURAS
    contagem_dias = {}  #GUARDA QUANTOS DIAS AQUELES MÊS TEVE
    dicMedias = {}  #DICIONÁRIO COM AS MÉDIAS DE CADA MÊS

    #FILTRANDO O MÊS E O ANO:
    for linha in listaDadosClimaticos:
        datas = linha["DATA"].split("/")
        mes_linha = int(datas[1])
        ano_linha = int(datas[2])
        temp_min = linha["TEMPMINIMA"]

        #SE FOR O MÊS ESCOLHIDO E ESTIVER NO INTERVALO:
        if mes_linha == mes_analise and 2006 <= ano_linha <= 2016:
            #CRIA A CHAVE:
            chave = f"{nome_mes_extenso}{ano_linha}"

            #ACUMULANDO A SOMA E OS DIAS:
            if chave in dicSomas:
                dicSomas[chave] += temp_min
                contagem_dias[chave] += 1
            else:
                dicSomas[chave] = temp_min
                contagem_dias[chave] = 1

    #CALCULANDO AS MÉDIAS:
    for chave in dicSomas:
        dicMedias[chave] = dicSomas[chave] / contagem_dias[chave]

    #EXIBINDO OS RESULTADOS:
    print(f"\nResultados para o mês de {nome_mes_extenso.upper()}:")
    print(f"{'CHAVE (Mês/Ano)':<20} | {'MÉDIA TEMP. MÍNIMA':<18}")

    #EXIBIÇÃO ANO A ANO DO MÊS SELECIONADO:
    for ano in range(2006, 2017):
        chave_busca = f"{nome_mes_extenso}{ano}"
        if chave_busca in dicMedias:
            print(f"{chave_busca:<20} | {dicMedias[chave_busca]:>14.2f} °C")
        else:
            print(f"{chave_busca:<20} | Dados não encontrados")

    return dicMedias, nome_mes_extenso

#===============================================================================================================

#FUNÇÃO PARA GERAR O GRÁFICO DE BARRAS:
def gerarGraficoBarras(dicMedias, nome_mes):

    #SEPARANDO CHAVES (EIXO X) E VALORES (EIXO Y):
    anos = [chave.replace(nome_mes, "") for chave in dicMedias.keys()]
    medias = list(dicMedias.values())

    #JANELA DO GRÁFICO
    plt.figure(figsize=(10, 6))

    #DESENHAR AS BARRAS:
    barras = plt.bar(anos, medias, color='#3498db', edgecolor='#2980b9', zorder=3)

    #TITULO E RÓTULOS:
    plt.title(f"Média da Temperatura Mínima para o Mês de {nome_mes.upper()} (2006 - 2016)\nPorto Alegre - RS",
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Anos Analisados", fontsize=12, fontweight='bold', labelpad=10)
    plt.ylabel("Temperatura Mínima Média (°C)", fontsize=12, fontweight='bold', labelpad=10)

    #GRADE FUNDO:
    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

    #ORGANIZANDO O GRÁFICO:
    for barra in barras:
        altura = barra.get_height()
        plt.annotate(f'{altura:.1f}°C',
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    #AJUSTE DE LAYOUT:
    plt.tight_layout()

    #EXIBINDO O GRÁFICO:
    plt.show()

#===============================================================================================================

# FUNÇÃO PARA CALCULAR A MÉDIA GERAL DO PERÍODO:
def mediaGeralPeriodo(dicMedias, nome_mes):
    soma_geral = 0.0
    quantidade_anos = len(dicMedias) #ANOS CALCULADOS

    #PERCORRE  DICIONÁRIO SOMANDO OS VALORES:
    for media_ano in dicMedias.values():
        soma_geral += media_ano

    #CÁLCULO DA MÉDIA GERAL:
    media_geral = soma_geral / quantidade_anos

    #EXIBE A MÉDIA GERAL:
    print("\nRESUMO ESTATÍSTICO GERAL")
    print(f"Mês analisado: {nome_mes.upper()}")
    print(f"Período: 2006 a 2016 ({quantidade_anos} anos)")
    print(f"Média geral da temperatura mínima: {media_geral:.2f} °C")

#===============================================================================================================

#PROGRAMA FEITO APENAS COM AS FUNÇÕES:

#ANÁLISE DE DADOS CONFORME INTERVALO INFORMADO PELO USUÁRIO:
periododoUsuario()

#MÊS MAIS CHUVOSO:
mesChuvoso()

#TEMP MINIMA DETERMINADO MÊS:
dicionario_calculado, mes_escolhido = mediaTempMinima()

#GRÁFICO DE BARRAS:
gerarGraficoBarras(dicionario_calculado, mes_escolhido)

#MÉDIA GERAL DA TEMPERATURA DE UM MÊS(EXIBIDO APÓS FECHAR O GRÁFICO):
mediaGeralPeriodo(dicionario_calculado, mes_escolhido)