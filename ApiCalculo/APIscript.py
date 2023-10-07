from datetime import date, datetime
from math import pow
import os
from time import sleep
import psutil
from colorama import Fore, Back, Style
import mysql.connector
import mysql.connector.errorcode
import json
import requests
from requests.auth import HTTPBasicAuth
import json
from jira import JIRA

jira_token = "ATATT3xFfGF0aXVjL68JsNQDXa24_XV67nnBFeWfkRw0qMqMefnku35UjV4tfuM1su6ygv3AZxVwnhXu8_wt-Kg-thakUGcUFJfTamHFhp1XXr3D9yvL5yKSXnzNsPbjLbs7UfSOzgN8fhaX_9kQAFaACBQpiyKGWPk2Vtes0YEiNbr6xd136H4=1116E5CD"
url = "https://greycloudtransactions.atlassian.net/rest/api/2/search"
server_name = "https://greycloudtransactions.atlassian.net"
email = 'GrayCloudTransactions@hotmail.com'

jira_connection = JIRA(
    basic_auth=(email, jira_token),
    server=server_name
)

issue_dict = {
    'project': {'key': 'GRCT'},
    'summary': "Testing issue from Python Jira Handbook",
    'description': 'Detailed ticket description.',
    'issuetype': {'id': '10007'}, 
}

new_issue = jira_connection.create_issue(fields=issue_dict)

visualizacaoDesejada = 0

conexao = mysql.connector.connect(
        host = "localhost",
        user = "aluno",
        password = "sptech",
        port = 3306,
        database = "ScriptGCT"
        )

comando = conexao.cursor()

def MostrarMsgGCT():
    print("=" * 100)
    print(
    """

     ██████╗ ██████╗ ███████╗██╗   ██╗
    ██╔════╝ ██╔══██╗██╔════╝╚██╗ ██╔╝
    ██║  ██╗ ██████╔╝█████╗   ╚████╔╝
    ██║  ╚██╗██╔══██╗██╔══╝    ╚██╔╝
    ╚██████╔╝██║  ██║███████╗   ██║
     ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝

     █████╗ ██╗      █████╗ ██╗   ██╗██████╗
    ██╔══██╗██║     ██╔══██╗██║   ██║██╔══██╗
    ██║  ╚═╝██║     ██║  ██║██║   ██║██║  ██║
    ██║  ██╗██║     ██║  ██║██║   ██║██║  ██║
    ╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝
     ╚════╝ ╚══════╝ ╚════╝  ╚═════╝ ╚═════╝

    ████████╗██████╗  █████╗ ███╗  ██╗ ██████╗ █████╗  █████╗ ████████╗██╗ █████╗ ███╗  ██╗ ██████╗
    ╚══██╔══╝██╔══██╗██╔══██╗████╗ ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗ ██║██╔════╝
       ██║   ██████╔╝███████║██╔██╗██║╚█████╗ ███████║██║  ╚═╝   ██║   ██║██║  ██║██╔██╗██║╚█████╗ 
       ██║   ██╔══██╗██╔══██║██║╚████║ ╚═══██╗██╔══██║██║  ██╗   ██║   ██║██║  ██║██║╚████║ ╚═══██╗
       ██║   ██║  ██║██║  ██║██║ ╚███║██████╔╝██║  ██║╚█████╔╝   ██║   ██║╚█████╔╝██║ ╚███║██████╔╝
       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝ ╚════╝    ╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚══╝╚═════╝ 
    """
    )
    print("=" * 100)

def bannerCpu():
    print(
        """
                                      █████╗ ██████╗ ██╗   ██╗
                                     ██╔══██╗██╔══██╗██║   ██║
___________________________________  ██║  ╚═╝██████╔╝██║   ██║  ___________________________________
                                     ██║  ██╗██╔═══╝ ██║   ██║
                                     ╚█████╔╝██║     ╚██████╔╝
                                      ╚════╝ ╚═╝      ╚═════╝
"""
    )

def bannerDisco():
    print(
        """
           ██████╗ ██╗ ██████╗ █████╗  █████╗   ██╗      █████╗  █████╗  █████╗ ██╗
           ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗  ██║     ██╔══██╗██╔══██╗██╔══██╗██║
_________  ██║  ██║██║╚█████╗ ██║  ╚═╝██║  ██║  ██║     ██║  ██║██║  ╚═╝███████║██║       _________
           ██║  ██║██║ ╚═══██╗██║  ██╗██║  ██║  ██║     ██║  ██║██║  ██╗██╔══██║██║     
           ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝  ███████╗╚█████╔╝╚█████╔╝██║  ██║███████╗
           ╚═════╝ ╚═╝╚═════╝  ╚════╝  ╚════╝   ╚══════╝ ╚════╝  ╚════╝ ╚═   ╚═╝╚══════╝     
"""
    )

def bannerMemoria():
    print(
        """

      ███╗   ███╗███████╗███╗   ███╗ █████╗ ██████╗ ██╗ █████╗   ██████╗  █████╗ ███╗   ███╗ 
      ████╗ ████║██╔════╝████╗ ████║██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗████╗ ████║
____  ██╔████╔██║█████╗  ██╔████╔██║██║  ██║██████╔╝██║███████║  ██████╔╝███████║██╔████╔██║  _____
      ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║  ██║██╔══██╗██║██╔══██║  ██╔══██╗██╔══██║██║╚██╔╝██║
      ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚█████╔╝██║  ██║██║██║  ██║  ██║  ██║██║  ██║██║ ╚═╝ ██║
      ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
    )

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Caso seja utilizado no Windows
        command = 'cls'
    os.system(command)


def MostrarValoresCPU():
    porcentagemUtilizacaoCPU = psutil.cpu_percent()
    porcentagemUtilizacaoCore = []
    qtdCores = psutil.cpu_count(logical=False)
    qtdThreads = psutil.cpu_count()

    temposCpu = psutil.cpu_times()
    porcentagemUtilizacaoCore = psutil.cpu_percent(percpu=True)
    porcentagemUtilizacaoCPU = psutil.cpu_percent()
    frequenciaCpu = psutil.cpu_freq()

    

    
    #conexao.close()

    bannerCpu()
    print('-' * 100)
    print("\n" + "Quantidade de Cores: " + str(qtdCores) + "\nQuantidade Threads: " + str(qtdThreads) + "\n")
    print('-' * 100)

    print((" " * 45) + "Tempos da CPU: \n")
    print("Tempo gasto pelos processos do Usuário (user): " + str(temposCpu.user) + "s" +  "\n"
            + "Tempo gasto pelo sistema (system): " + str(temposCpu.system) + "s" + "\n"
            + "Tempo Ocioso (idle): " + str(temposCpu.idle) + "s" + "\n")


    print('-' * 100 + "\n")     
    print((" " * 35) + "Porcentagem de Utilização da CPU: \n")
    if(porcentagemUtilizacaoCPU > 70):
        print("\n" + "Utilização da Total da CPU:" + Fore.RED+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    elif porcentagemUtilizacaoCPU > 20 :
        print("\n" + "Utilização da Total da CPU:" + Fore.YELLOW+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    else :
        print("\n" + "Utilização da Total da CPU:" + Fore.GREEN+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    
    
    for i in range(len(porcentagemUtilizacaoCore)):
        if(porcentagemUtilizacaoCore[i] > 70):
            print("Thread " + str(i + 1) + ": "+ Fore.RED  + str(porcentagemUtilizacaoCore[i]) + "%" + Style.RESET_ALL)
        elif porcentagemUtilizacaoCore[i] > 50 :
                print("Thread " + str(i + 1) + ": "+ Fore.YELLOW  + str(porcentagemUtilizacaoCore[i]) + "%" + Style.RESET_ALL)
                mensagemCpu = {"text": f"""
                    ⚙️ === ALERTA❗️
                    Descrição => Sua CPU está sobrecarregando!
                    """}
                chatMonitoramentoCpu = "https://hooks.slack.com/services/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"
                postMsgCpu = requests.post(chatMonitoramentoCpu, data=json.dumps(mensagemCpu))
                print(postMsgCpu.status_code)
        else :
            print("Thread " + str(i + 1) + ": "+ Fore.GREEN  + str(porcentagemUtilizacaoCore[i]) + "%" + Style.RESET_ALL)
    
    print("-" * 100)

    print((" "*45) + "Frequência da CPU")
    print("Frequência Atual: " + str(round(frequenciaCpu.current, 2)) + "MHz" + "\n"
            + "Frequência Mínima: " + str(frequenciaCpu.min)+ "MHz" + "\n"
            + "Frequência Máxima: " + str(frequenciaCpu.max)+ "MHz" + "\n")
    print("-" * 100)
    

    UtilizacaoCore = "{:.0f}".format(porcentagemUtilizacaoCore[i]); 
    freqCpuMin = "{:.0f}".format(frequenciaCpu.min);
    dataHoraNow = datetime.now();


    # comando.execute("INSERT INTO Registro(idServidor, tipoRegistro, valorRegistro, unidadeRegistro, dateNow) VALUES" 
    #                 f"(1,'Quantidade de Cores', '{qtdCores}', 'null', '{dataHoraNow}')," +
    #                 f"(1,'Quantidade de Threads', '{qtdThreads}', 'null','{dataHoraNow}')," +
    #                 f"(1,'Tempo CPU User','{temposCpu.user}','segundos','{dataHoraNow}')," +
    #                 f"(1,'Tempo CPU System','{temposCpu.system}','segundos','{dataHoraNow}')," +
    #                 f"(1,'Tempo CPU Idle','{temposCpu.idle}','segundos','{dataHoraNow}')," +
    #                 f"(1,'Porcentagem Utilizada Core', '{UtilizacaoCore}', '%','{dataHoraNow}')," + 
    #                 f"(1,'Porcentagem Utilizada CPU', '{porcentagemUtilizacaoCPU}', '%','{dataHoraNow}')," + 
    #                 f"(1,'Frequência CPU', '{frequenciaCpu.current}', 'MHz','{dataHoraNow}')," +
    #                 f"(1,'Freq. CPU Min.','{frequenciaCpu.min}', 'MHz','{dataHoraNow}')," +
    #                 f"(1,'Freq. CPU Max.','{frequenciaCpu.max}', 'MHz','{dataHoraNow}')");

    comando.execute("INSERT INTO `registro`(valor_registro, data_registro, fk_modelo_componente) VALUES" 
                    f"('{qtdCores}', '{dataHoraNow}', 1)," +
                    f"('{qtdThreads}', '{dataHoraNow}', 1)," +
                    f"('{temposCpu.user}', '{dataHoraNow}', 1)," +
                    f"('{temposCpu.system}', '{dataHoraNow}', 1)," +
                    f"('{temposCpu.idle}', '{dataHoraNow}', 1)," +
                    f"('{UtilizacaoCore}', '{dataHoraNow}', 1)," + 
                    f"('{porcentagemUtilizacaoCPU}', '{dataHoraNow}', 1)," + 
                    f"('{frequenciaCpu.current}', '{dataHoraNow}', 1)," +
                    f"('{frequenciaCpu.min}', '{dataHoraNow}', 1)," +
                    f"('{frequenciaCpu.max}', '{dataHoraNow}', 1)");
    
    # print("No of Record Inserted :", comando.rowcount) 
    #print("Inserted Id :", comando.lastrowid) 
conexao.commit()  
    
    
    
print("=" * 100)


def MostrarValoresDiscoLocal():

    totalDisco = psutil.disk_usage('/').total
    sendoUsado = psutil.disk_usage('/').used
    espacoLivre = psutil.disk_usage('/').free
    porcentagemEmUso = psutil.disk_usage('/').percent

    # byteToMegabyteTotal = (float(totalDisco) / 1024)
    # byteToMegabyteUsando = (float(sendoUsado) / 1024)
    # byteToMegabyteLivre = (float(espacoLivre) / 1024)

    byteToGigabyteTotal = (float(totalDisco) * (1 * pow(10,-9)))
    byteToGigabyteUsando = (float(sendoUsado) * (1 * pow(10,-9)))
    byteToGigabyteLivre = (float(espacoLivre) * (1 * pow(10,-9)))

    # megaByteToGigabyteTotal = byteToMegabyteTotal / 1024
    # megaByteToGigabyteUsando = byteToMegabyteUsando / 1024
    # megaByteToGigabyteLivre = byteToMegabyteLivre / 1024

    # gigaByteToTerabyte = megaByteToGigabyte / 1024



    formatted_total1 = "{:.2f}".format(byteToGigabyteTotal)
    formatted_total2 = "{:.2f}".format(byteToGigabyteUsando)
    formatted_total3 = "{:.2f}".format(byteToGigabyteLivre)

    # print("\nQuantidade total(GB): " + str(megaByteToGigabyteTotal))
    # print("\nQuantidade em uso(GB): " + str(megaByteToGigabyteUsando))
    # print("\nEm uso: " + str(porcentagemEmUso) + "%" + " (com base no total e na quantidade em uso.)")
    # print("\nQuantidade livre(GB): " + str(megaByteToGigabyteLivre) + "\n")

    bannerDisco()
    print("-" * 100)
    print((" " * 40) + "Dados da Memória de Massa: \n")
    print("-" * 100)
    print("\nDe bytes para Gigabytes: ")
    print("\nQuantidade total: " + Fore.BLUE + str(formatted_total1) + " GB" + Style.RESET_ALL + "\n")
    print("Quantidade livre: " + Fore.BLUE + str(formatted_total3) + " GB" + Style.RESET_ALL + "\n")
    print("Quantidade em uso: " + Fore.BLUE + str(formatted_total2) + " GB" + Style.RESET_ALL + "\n")
# print("Em uso: " + str(porcentagemEmUso) + "%" + " (com base no total e na quantidade em uso.)")

    if(porcentagemEmUso > 70):
        print("\n" + "Em uso: " + Fore.RED + str(porcentagemEmUso) + "%" + Style.RESET_ALL + "\n")
    elif porcentagemEmUso > 50 :
        print("\n" + "Em uso: " + Fore.YELLOW + str(porcentagemEmUso) + "%" + Style.RESET_ALL + "\n")
        mensagemDisco = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Seu Disco está sobrecarregando!
            """}
        chatMonitoramentoDisco = "https://hooks.slack.com/services/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"
        postMsgDisco = requests.post(chatMonitoramentoDisco, data=json.dumps(mensagemDisco))
        print(postMsgDisco.status_code)
    else :
        print("\n" + "Em uso: " + Fore.GREEN + str(porcentagemEmUso) + "%" + Style.RESET_ALL + "\n")
    
    print('-' * 100)

    print("Informações sem tratamento:\n")
    print('-' * 100)
    print(psutil.disk_usage('/'))

    dataHoraNow = datetime.now()

    # comando.execute("INSERT INTO Registro(idServidor, tipoRegistro, valorRegistro, unidadeRegistro, dateNow) VALUES" 
    #                 f"(1,'Quantidade total de memória de massa', '{formatted_total1}', 'Gigabytes', '{dataHoraNow}')," +
    #                 f"(1,'Quantidade livre de memória de massa', '{formatted_total3}', 'Gigabytes', '{dataHoraNow}')," +
    #                 f"(1,'Quantidade de memória de massa em uso','{formatted_total2}','Gigabytes', '{dataHoraNow}')," +
    #                 f"(1,'Memória de massa em uso','{porcentagemEmUso}','%', '{dataHoraNow}')");
    comando.execute("INSERT INTO `registro`(valor_registro, data_registro, fk_modelo_componente) VALUES" 
                    f"('{formatted_total1}', '{dataHoraNow}', 1)," +
                    f"('{formatted_total3}', '{dataHoraNow}', 1)," +
                    f"('{formatted_total2}', '{dataHoraNow}', 1)," +
                    f"('{porcentagemEmUso}', '{dataHoraNow}', 1)");

    conexao.commit();
    


    print("=" * 100)
        

# Fim das Info Disco Local
def MostrarValoresRAM():

    valoresMemoriaRam = psutil.virtual_memory()
    ramTotal = valoresMemoriaRam.total
    ramDisponivel = valoresMemoriaRam.available
    ramPercentualUtilizado = valoresMemoriaRam.percent
    ramUtilizando = valoresMemoriaRam.used
    ramLivre = valoresMemoriaRam.free

    ramByteToGigabyteTotal = (float(ramTotal) * (1 * pow(10,-9)))
    ramByteToGigabyteUsando = (float(ramUtilizando) * (1 * pow(10,-9)))
    ramByteToGigabyteDisponivel = (float(ramDisponivel) * (1 * pow(10,-9)))
    ramByteToGigabyteLivre = (float(ramLivre) * (1 * pow(10,-9)))

    bannerMemoria()
    print("-" * 100)
    print((" " * 37) + "Dados da Memória Virtual: \n")
    print("-" * 100)
    print("Memória RAM total: " + Fore.BLUE + "{:.2f}".format(ramByteToGigabyteTotal) + " GB" + Style.RESET_ALL + "\n")
    print( "Memória RAM disponível: " + Fore.BLUE + "{:.2f}".format(ramByteToGigabyteDisponivel) + " GB" + Style.RESET_ALL + "\n")
    print( "Memória RAM usado: " + Fore.BLUE + "{:.2f}".format(ramByteToGigabyteUsando) + " GB" + Style.RESET_ALL + "\n")
    print( "Memória RAM livre: " + Fore.BLUE + "{:.2f}".format(ramByteToGigabyteLivre) + " GB" + Style.RESET_ALL + "\n")

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
        
        
    print('-' * 100)
    print(valoresMemoriaRam)

    dataHoraNow = datetime.now()

    # comando.execute("INSERT INTO Registro(idServidor, tipoRegistro, valorRegistro, unidadeRegistro, dateNow) VALUES" 
    #                     f"(1,'Memória RAM total', '{ramByteToGigabyteTotal}', 'Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM disponível', '{ramByteToGigabyteDisponivel}', 'Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM usado','{ramByteToGigabyteUsando}','Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM livre','{ramByteToGigabyteLivre}','Gigabytes', '{dataHoraNow}')," +
    #                     f"(1,'Memória RAM em uso','{ramPercentualUtilizado}','%', '{dataHoraNow}')");
    
    comando.execute("INSERT INTO `registro`(valor_registro, data_registro, fk_modelo_componente) VALUES" 
                        f"('{ramByteToGigabyteTotal}', '{dataHoraNow}', 1)," +
                        f"('{ramByteToGigabyteDisponivel}', '{dataHoraNow}', 1)," +
                        f"('{ramByteToGigabyteUsando}', '{dataHoraNow}', 1)," +
                        f"('{ramByteToGigabyteLivre}', '{dataHoraNow}', 1)," +
                        f"('{ramPercentualUtilizado}', '{dataHoraNow}', 1)");

    conexao.commit();



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
