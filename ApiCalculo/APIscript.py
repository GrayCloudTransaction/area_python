from datetime import datetime
from math import pow
from time import sleep
import psutil
from colorama import Fore, Back, Style
import mysql.connector
import mysql.connector.errorcode
import json
import requests
import json
from jira import JIRA
from API_script_terminal import *

jira_token = "ATATT3xFfGF0l5bpDf9hQkJDGmZrKKmDnzwCk4Gh27zc_pS9WyyDtsMBZJe-ah7wEsyq3Ck_HG3Frvh-loVWJXFUdCaB9wvFTeN-N0pLGlXAHW1BVdYfN6XrOsO6aAbfKO_0W8VPVaXWXBYy7h_YXpYtfFS39rDqjWNhPn-9N7UlhFn8GX6kTyQ=517218CC"
url = "https://greycloudtransactions.atlassian.net/rest/api/2/search"
server_name = "https://greycloudtransactions.atlassian.net"
email = 'GrayCloudTransactions@hotmail.com'

jira_connection = JIRA(
    basic_auth=(email, jira_token),
    server=server_name
)

#issue_dict = {
#    'project': {'key': 'SUP'},
#    'summary': "Testing issue from Python Jira Handbook",
#    'description': 'Detailed ticket description.',
#    'issuetype': {"id":"10022"},
#}

#new_issue = jira_connection.create_issue(fields=issue_dict)


visualizacaoDesejada = 0

conexao = mysql.connector.connect(
        host = "localhost",
        user = "aluno",
        password = "sptech",
        port = 3306,
        database = "ScriptGCT"
    )

comando = conexao.cursor()

def MostrarValoresCPU():
    porcentagemUtilizacaoCPU = psutil.cpu_percent()
    qtdThreads = psutil.cpu_count()
    
    #conexao.close()

    bannerCpu()

    print('-' * 100 + "\n")     
    print((" " * 35) + "Porcentagem de Utilização da CPU: \n")
    if(porcentagemUtilizacaoCPU > 70):
        print("\n" + "Utilização da Total da CPU:" + Fore.RED+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    elif porcentagemUtilizacaoCPU > 50 :
        print("\n" + "Utilização da Total da CPU:" + Fore.YELLOW+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    else :
        print("\n" + "Utilização da Total da CPU:" + Fore.GREEN+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    
    
    print("-" * 100)

    dataHoraNow = datetime.now()

    
    comando.execute("INSERT INTO registro (valor_registro, data_registro, fk_medida, fk_componente) VALUES" 
                    f"({porcentagemUtilizacaoCPU}, '{dataHoraNow}', 1);")
    
    # print("No of Record Inserted :", comando.rowcount) 
    # print("Inserted Id :", comando.lastrowid) 

conexao.commit()

def MostrarValoresDiscoLocal():
    porcentagem_livre = 100 - psutil.disk_usage('/').percent

    bannerDisco()
    print("-" * 100)
    print((" " * 40) + "Dados da Memória de Massa: \n")
    print("-" * 100)
    print("\nDe bytes para Gigabytes: ")

    if(porcentagem_livre < 40):
        print("\n" + "Em uso: " + Fore.YELLOW + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
    elif porcentagem_livre < 20 :
        print("\n" + "Em uso: " + Fore.RED + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
        mensagemDisco = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Seu Disco está sobrecarregando!
            """}
        chatMonitoramentoDisco = "https://hooks.slack.com/services/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"
        postMsgDisco = requests.post(chatMonitoramentoDisco, data=json.dumps(mensagemDisco))
        print(postMsgDisco.status_code)
    else :
        print("\n" + "Em uso: " + Fore.GREEN + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
    
    print('-' * 100)

    print("Informações sem tratamento:\n")
    print('-' * 100)
    print(psutil.disk_usage('/'))

    dataHoraNow = datetime.now()

    comando.execute("INSERT INTO `registro`(valor_registro, data_registro, fk_medida, fk_componente) VALUES" 
                    f"('{porcentagem_livre}', '{dataHoraNow}', 1,1);")

    conexao.commit()
    


    print("=" * 100)
        

# Fim das Info Disco Local
def MostrarValoresRAM():

    valoresMemoriaRam = psutil.virtual_memory()
    ramPercentualUtilizado = valoresMemoriaRam.percent

    swap = psutil.swap_memory().percent

    bannerMemoria()
    print("-" * 100)
    print((" " * 37) + "Dados da Memória Virtual: \n")
    print("-" * 100)

    # print( "Memória RAM percentual: " + Fore.BLUE + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")

    print('-' * 100)

    if(ramPercentualUtilizado > 70):
            print("\n" + "Em uso: " + Fore.RED + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
    elif ramPercentualUtilizado > 50 :
            print("\n" + "Em uso: " + Fore.YELLOW + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
            mensagemRam = {"text": f"""
                ⚙️ === ALERTA❗️
                Descrição => Sua Memória RAM está sobrecarregando!
                """}
            chatMonitoramentoRam = "https://hooks.slack.com/services/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"
            postMsgRam = requests.post(chatMonitoramentoRam, data=json.dumps(mensagemRam))
            print(postMsgRam.status_code)
    else :
            print("\n" + "Em uso: " + Fore.GREEN + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
        
    if(swap < 30 and swap > 20):
            print("\n" + "Em uso: " + Fore.YELLOW + str(swap) + "%" + Style.RESET_ALL + "\n")
    elif swap > 30 :
            print("\n" + "Em uso: " + Fore.RED + str(swap) + "%" + Style.RESET_ALL + "\n")
            mensagemSwap = {"text": f"""
                ⚙️ === ALERTA❗️
                Descrição => Sua Memória SWAP está sobrecarregando!
                """}
            chatMonitoramentoSwap = "https://hooks.slack.com/services/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"
            postMsgSwap = requests.post(chatMonitoramentoSwap, data=json.dumps(mensagemSwap))
            print(postMsgSwap.status_code)
    else :
            print("\n" + "Em uso: " + Fore.GREEN + str(swap) + "%" + Style.RESET_ALL + "\n")
        
    print('-' * 100)
    print(valoresMemoriaRam)

    dataHoraNow = datetime.now()

    # comando.execute("INSERT INTO Registro(idServidor, tipoRegistro, valorRegistro, unidadeRegistro, dateNow) VALUES" 
    #                     f"(1,'Memória RAM total', '{ramByteToGigabyteTotal}', 'Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM disponível', '{ramByteToGigabyteDisponivel}', 'Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM usado','{ramByteToGigabyteUsando}','Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM livre','{ramByteToGigabyteLivre}','Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM em uso','{ramPercentualUtilizado}','%', '{dataHoraNow}')");
    
    comando.execute("INSERT INTO `registro`(valor_registro, data_registro, fk_medida, fk_componente) VALUES" 
                        f"('{ramPercentualUtilizado}', '{dataHoraNow}', 1, 1);")

    conexao.commit()



    print("=" * 100)

def MostrarValores(visuDesejada):
    visualizacaoDesejada = visuDesejada
    if visualizacaoDesejada == 1:
        for i in range(0, 10):
            clearConsole()
            MostrarValoresCPU()
            sleep(2)
            clearConsole()
    elif visualizacaoDesejada == 2:
        for i in range(0, 10):
            clearConsole()
            MostrarValoresDiscoLocal()
            sleep(2)
            clearConsole()
    elif visualizacaoDesejada == 3:
        for i in range(0, 10):
            clearConsole()
            MostrarValoresRAM()
            sleep(2)
            clearConsole()
    elif (visualizacaoDesejada == 4):
        for i in range(0, 10):
            clearConsole()
            MostrarValoresCPU()
            MostrarValoresDiscoLocal()
            MostrarValoresRAM()
            sleep(2)
            clearConsole()
    elif visualizacaoDesejada == 0:
        print("\n☁️  Até logo!")
        exit()
    voltar = int(input("0 = Voltar a seleção de componentes \n1 = Continuar a captação de dados \n=> "))
    while voltar != 0 and voltar != 1:
        voltar = int(input("0 = Voltar a seleção de componentes \n1 = Continuar a captação de dados \n=> "))
    if voltar == 1:
        MostrarValores(visualizacaoDesejada)
    elif voltar == 0:
        print(visualizacaoDesejada)
        MensagemTeste()

def MensagemTeste():
    MostrarMsgGCT()
    visualizacaoDesejada = int(input("Escolha o componente que deseja visualizar \n1 = CPU \n2 = Disco Local \n3 = Memória RAM \n4 = Todos \n0 = Para finalizar o processo \n=> "))

    while visualizacaoDesejada != 1 and visualizacaoDesejada != 2 and visualizacaoDesejada != 3 and visualizacaoDesejada != 4 and visualizacaoDesejada != 0:
        
        visualizacaoDesejada = int(input("Escolha o componente que deseja visualizar \n1 = CPU \n2 = Disco Local \n3 = Memória RAM \n4 = Todos \n0 = Para finalizar o processo \n=> "))
    MostrarValores(visualizacaoDesejada)

# Mensagem inicial

MensagemTeste()
