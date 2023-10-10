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

jira_token = "ATATT3xFfGF004HezdV_tKYO8JymCLnHI9GQy24sHgCegDGJFlvCmHTFgUYTsnb4hmGQI8fqvO99SQRR7vqg1VS8b0OEwPOkGCVq75q6aTm4i5fziZDbPI50GuBvahn37l6CtRxYO53h9ashpYR2KMRFac26J-mv_ywDHEqVNQ6iFPuljxbvPcc=FF309C42"
url = "https://greycloudtransactions.atlassian.net/rest/api/2/search"
server_name = "https://greycloudtransactions.atlassian.net"
email = 'GrayCloudTransactions@hotmail.com'

jira_connection = JIRA(
    basic_auth=(email, jira_token),
    server=server_name
)

# issue_dict = {
#    'project': {'key': 'SUP'},
#    'summary': "Testing issue from Python Jira Handbook",
#    'description': 'Detailed ticket description.',
#    'issuetype': {"id":"10022"},
#}

#new_issue = jira_connection.create_issue(fields=issue_dict)


visualizacaoDesejada = 0

conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        port = 3306,
        database = "ScriptGCT"
    )

comando = conexao.cursor()

input_componente = int(input("Qual o id do componente "))

def MostrarValoresCPU(input_componente):
    porcentagemUtilizacaoCPU = psutil.cpu_percent()
    
    #conexao.close()

    bannerCpu()
    
    print('-' * 100 + "\n")     
    print((" " * 35) + "Porcentagem de Utilização da CPU: \n")
    if(porcentagemUtilizacaoCPU > 1):
        print("\n" + "Utilização da Total da CPU:" + Fore.RED+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
        
        issue_dict = {
            'project': {'key': 'SUP'},
            'summary': f"Componente está com mais de {porcentagemUtilizacaoCPU}% de uso da CPU!!! ",
            'description': f'O componente de disco com ID {input_componente} está com mais de {porcentagemUtilizacaoCPU}% de uso da CPU!!!',
            'issuetype': {"id":"10022"},
        }

        new_issue = jira_connection.create_issue(fields=issue_dict)
        
        mensagem_CPU = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Sua CPU está sobrecarregando!
            """}
        chatMonitoramentoCpu = "https://hooks.slack.com/services/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"
        postMsgCpu = requests.post(chatMonitoramentoCpu, data=json.dumps(mensagem_CPU))
        
    elif porcentagemUtilizacaoCPU > 50 :
        print("\n" + "Utilização da Total da CPU:" + Fore.YELLOW+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    else :
        print("\n" + "Utilização da Total da CPU:" + Fore.GREEN+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    
    
    print("-" * 100)

    dataHoraNow = datetime.now()
    
    comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente) VALUES" 
                    f"({porcentagemUtilizacaoCPU}, '{dataHoraNow}', {input_componente});")
    
    conexao.commit()

def MostrarValoresDiscoLocal(input_componente):
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
        
        issue_dict = {
            'project': {'key': 'SUP'},
            'summary': f"Componente está com apenas {porcentagem_livre}% de espaço livre!!!",
            'description': f'O componente de disco com ID {input_componente} está com apenas {porcentagem_livre}% de espaço livre!!!',
            'issuetype': {"id":"10022"},
        }

        new_issue = jira_connection.create_issue(fields=issue_dict)
        
        print(postMsgDisco.status_code)
    else :
        print("\n" + "Em uso: " + Fore.GREEN + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
    
    print('-' * 100)

    print("Informações sem tratamento:\n")
    print('-' * 100)
    print(psutil.disk_usage('/'))

    dataHoraNow = datetime.now()
    comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente) VALUES" 
                    f"('{porcentagem_livre}', '{dataHoraNow}',${input_componente});")

    conexao.commit()

    print("=" * 100)
        

# Fim das Info Disco Local
def MostrarValoresRAM(input_componente):

    valoresMemoriaRam = psutil.virtual_memory()
    ramPercentualUtilizado = valoresMemoriaRam.percent

    swap = psutil.swap_memory().percent

    bannerMemoria()
    print("-" * 100)
    print((" " * 37) + "Dados da Memória Virtual: \n")
    print("-" * 100)

    print('-' * 100)

    if(ramPercentualUtilizado > 70):
        print("\n" + "Em uso: " + Fore.RED + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
        mensagemRam = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Sua Memória RAM está sobrecarregando!
            """}
        chatMonitoramentoRam = "https://hooks.slack.com/services/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"
        postMsgRam = requests.post(chatMonitoramentoRam, data=json.dumps(mensagemRam))
        print(postMsgRam.status_code)
        
        issue_dict = {
            'project': {'key': 'SUP'},
                'summary': f"Componente está com mais de {ramPercentualUtilizado}% de uso da memória RAM!!! ",
            'description': f'O componente de disco com ID {ramPercentualUtilizado} está com mais de {ramPercentualUtilizado}% de uso da memória RAM!!!',
            'issuetype': {"id":"10022"},
        }
        new_issue = jira_connection.create_issue(fields=issue_dict)
            
    elif ramPercentualUtilizado > 50 :
        print("\n" + "Em uso: " + Fore.YELLOW + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
        
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
            
            issue_dict = {
                'project': {'key': 'SUP'},
                'summary': f"Disco está com mais de {swap}% de uso da memória swap!!! ",
                'description': f'O componente de disco com ID {input_componente} está com mais de {swap}% de uso da memória swap!!!',
                'issuetype': {"id":"10022"},
            }

            new_issue = jira_connection.create_issue(fields=issue_dict)
            
    else:
            print("\n" + "Em uso: " + Fore.GREEN + str(swap) + "%" + Style.RESET_ALL + "\n")
        
    print('-' * 100)
    print(valoresMemoriaRam)

    dataHoraNow = datetime.now()

    comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente) VALUES" 
                        f"('{ramPercentualUtilizado}', '{dataHoraNow}', {input_componente});")

    conexao.commit()

    print("=" * 100)

def MostrarValores(visuDesejada):
    visualizacaoDesejada = visuDesejada
    if visualizacaoDesejada == 1:
        for i in range(0, 1):
            clearConsole()
            MostrarValoresCPU(input_componente)
            sleep(2)
            clearConsole()
    elif visualizacaoDesejada == 2:
        for i in range(0, 10):
            clearConsole()
            MostrarValoresDiscoLocal(input_componente)
            sleep(2)
            clearConsole()
    elif visualizacaoDesejada == 3:
        for i in range(0, 10):
            clearConsole()
            MostrarValoresRAM(input_componente)
            sleep(2)
            clearConsole()
    elif (visualizacaoDesejada == 4):
        for i in range(0, 10):
            clearConsole()
            MostrarValoresCPU(input_componente)
            MostrarValoresDiscoLocal(input_componente)
            MostrarValoresRAM(input_componente)
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
