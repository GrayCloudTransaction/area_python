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


jira_token = "ATATT3xFfGF0UmWAi-LW5-Bx1_c9B-sQs5GV_f-eKkA6clUdYwh-r0hlBKeRg2EJQZ9d9YtVZbf4UsWfopgvkj8nBdiHjX_9vM_ZnBg2zmOnFLA-mH_Ri_efGg-QjKJFnSdZwDfem7vP3LDi8nDIiQG1GE3QEDrEN8tZZ8_xeWUVIm_VuGEgKJo=6345AAD2"
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
        user = "aluno",
        password = "sptech",
        port = 3306,
        database = "ScriptGCT"
    )

comando = conexao.cursor()

def login():
    lista_codigos = []
    select_componentes = []
    modo_ativar_login = True

    if modo_ativar_login == True:
        comando.execute(f"SELECT componente.* from componente, servidor where codigo = 'XPTO-0987';")
        select_componentes = comando.fetchall()
        
        comando.execute(f"SELECT id_servidor FROM servidor WHERE codigo = 'XPTO-0987';")
        id_servidor = comando.fetchall()
                    
        return select_componentes, id_servidor

    while modo_ativar_login:
        while True:
            MostrarMsgGCT()
            print('LOGIN: ')
            email = input("Escreva o seu email: ")
            senha = input("Escreva sua senha: ")
            
            comando.execute(f"SELECT * FROM funcionario WHERE email = '{email}' and senha = '{senha}';")

            get_func = comando.fetchall()
            if len(get_func) == 1:
                break
        
            else:
                print("Nome ou senha incorretos")
                sleep(2)
                clearConsole()
                
                
        while True:    
            print("BEM VINDO!")
            comando.execute(f"SELECT servidor.* FROM servidor WHERE fk_empresa = {get_func[0][8]};")
            select_server_empresa = comando.fetchall()
            
            print("Começar captura de dados! selecione o codigo do servidor \n")
            
            for i in select_server_empresa:
                print(i[2], i[1])
                lista_codigos.append(i[2])
            while True:
                codigo = input("\nCodigo do servidor: ")
            
                try:
                    lista_codigos.index(codigo)
                
                except ValueError:
                    print("Codigo errado!")
                else:
                    comando.execute(f"SELECT componente.* from componente, servidor where codigo = '{codigo}';")
                    select_componentes = comando.fetchall()
                    
                    comando.execute(f"SELECT id_servidor WHERE codigo = '{codigo}';")
                    id_servidor = comando.fetchall()
                    
                    print(id_servidor)
                    
                    if len(select_componentes) <= 0:
                        clearConsole()
                        print("Codigo errado ou servidor sem componentes cadastrados!")
                    
                    else:
                        return select_componentes
    
    
def MostrarValoresCPU(id_componente):
    porcentagemUtilizacaoCPU = psutil.cpu_percent()
    valor_risco = 0
    
    #conexao.close()

    bannerCpu()
    
    print('-' * 100 + "\n")     
    print((" " * 35) + "Porcentagem de Utilização da CPU: \n")
    if(porcentagemUtilizacaoCPU > 70):
        print("\n" + "Utilização da Total da CPU:" + Fore.RED+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
        
        issue_dict = {
            'project': {'key': 'SUP'},
            'summary': f"Componente está com mais de {porcentagemUtilizacaoCPU}% de uso da CPU!!! ",
            'description': f'O componente de disco com ID {id_componente} está com mais de {porcentagemUtilizacaoCPU}% de uso da CPU!!!',
            'issuetype': {"id":"10022"},
        }

        #new_issue = jira_connection.create_issue(fields=issue_dict)
        
        mensagem_CPU = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Sua CPU está sobrecarregando!
            """}
        chatMonitoramentoCpu = "https://hooks.slack.com/services/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"
        #postMsgCpu = requests.post(chatMonitoramentoCpu, data=json.dumps(mensagem_CPU))
        valor_risco = 4
        
        
    elif porcentagemUtilizacaoCPU > 50 :
        print("\n" + "Utilização da Total da CPU:" + Fore.YELLOW+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
        valor_risco = 1
    else :
        print("\n" + "Utilização da Total da CPU:" + Fore.GREEN+str(porcentagemUtilizacaoCPU) + "%" + Style.RESET_ALL + "\n")
    
    
    print("-" * 100)

    dataHoraNow = datetime.now()
    
    comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente, fk_medida) VALUES" 
                    f"({porcentagemUtilizacaoCPU}, '{dataHoraNow}', {id_componente}, 1);")
    
    conexao.commit()
    
    return valor_risco

def MostrarValoresDiscoLocal(id_componente):
    porcentagem_livre = 100 - psutil.disk_usage('/').percent
    porcentagem_livre = round(porcentagem_livre,2)
    
    valor_risco = 0

    bannerDisco()
    print("-" * 100)
    print((" " * 40) + "Dados da Memória de Massa: \n")
    print("-" * 100)
    print("\nDe bytes para Gigabytes: ")

    if(porcentagem_livre < 40):
        print("\n" + "Em uso: " + Fore.YELLOW + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
        valor_risco = 1
    elif porcentagem_livre < 20 :
        print("\n" + "Em uso: " + Fore.RED + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
        mensagemDisco = {"text": f"""
            ⚙️ === ALERTA❗️
            Descrição => Seu Disco está sobrecarregando!
            """}
        chatMonitoramentoDisco = "https://hooks.slack.com/services/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"
        #postMsgDisco = requests.post(chatMonitoramentoDisco, data=json.dumps(mensagemDisco))
        
        issue_dict = {
            'project': {'key': 'SUP'},
            'summary': f"Componente está com apenas {porcentagem_livre}% de espaço livre!!!",
            'description': f'O componente de disco com ID {id_componente} está com apenas {porcentagem_livre}% de espaço livre!!!',
            'issuetype': {"id":"10022"},
        }

        #new_issue = jira_connection.create_issue(fields=issue_dict)
        
        valor_risco = 4
    else:
        print("\n" + "Em uso: " + Fore.GREEN + str(porcentagem_livre) + "%" + Style.RESET_ALL + "\n")
    
    print('-' * 100)

    print("Informações sem tratamento:\n")
    print('-' * 100)
    print(psutil.disk_usage('/'))

    dataHoraNow = datetime.now()
    comando.execute(f"INSERT INTO `registro` (valor_registro, data_registro, fk_componente, fk_medida) VALUES" 
                    f"('{porcentagem_livre}', '{dataHoraNow}',{id_componente}, 1);")

    conexao.commit()

    print("=" * 100)
    return valor_risco    

# Fim das Info Disco Local
def MostrarValoresRAM(id_componente):
    valoresMemoriaRam = psutil.virtual_memory()
    ramPercentualUtilizado = valoresMemoriaRam.percent
    valor_risco = 0

    #swap = psutil.swap_memory().percent

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
        #postMsgRam = requests.post(chatMonitoramentoRam, data=json.dumps(mensagemRam))
        
        issue_dict = {
            'project': {'key': 'SUP'},
                'summary': f"Componente está com mais de {ramPercentualUtilizado}% de uso da memória RAM!!! ",
            'description': f'O componente de disco com ID {ramPercentualUtilizado} está com mais de {ramPercentualUtilizado}% de uso da memória RAM!!!',
            'issuetype': {"id":"10022"},
        }
        #new_issue = jira_connection.create_issue(fields=issue_dict)
        valor_risco = 4
            
    elif ramPercentualUtilizado > 50 :
        print("\n" + "Em uso: " + Fore.YELLOW + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
        valor_risco = 1
        
    else:
        print("\n" + "Em uso: " + Fore.GREEN + str(ramPercentualUtilizado) + "%" + Style.RESET_ALL + "\n")
        
        
    #if(swap < 30 and swap > 20):
    #        print("\n" + "Em uso: " + Fore.YELLOW + str(swap) + "%" + Style.RESET_ALL + "\n")
    #elif swap > 30 :
    #         print("\n" + "Em uso: " + Fore.RED + str(swap) + "%" + Style.RESET_ALL + "\n")
    #         mensagemSwap = {"text": f"""
    #             ⚙️ === ALERTA❗️
    #             Descrição => Sua Memória SWAP está sobrecarregando!
    #             """}
    #         chatMonitoramentoSwap = "https://hooks.slack.com/services/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"
    #         postMsgSwap = requests.post(chatMonitoramentoSwap, data=json.dumps(mensagemSwap))
    #         print(postMsgSwap.status_code)
            
    #         issue_dict = {
    #             'project': {'key': 'SUP'},
    #             'summary': f"Disco está com mais de {swap}% de uso da memória swap!!! ",
    #             'description': f'O componente de disco com ID {id_componente} está com mais de {swap}% de uso da memória swap!!!',
    #             'issuetype': {"id":"10022"},
    #         }

    #         #new_issue = jira_connection.create_issue(fields=issue_dict)
            
    # else:
    #     print("\n" + "Em uso: " + Fore.GREEN + str(swap) + "%" + Style.RESET_ALL + "\n")
        
    print('-' * 100)
    print(valoresMemoriaRam)

    dataHoraNow = datetime.now()

    comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente, fk_medida) VALUES" 
                        f"('{ramPercentualUtilizado}', '{dataHoraNow}', {id_componente}, 1);")
    
    # comando.execute(f"INSERT INTO `registro`(valor_registro, data_registro, fk_componente, fk_medida) VALUES" 
    #                     f"('{swap}', '{dataHoraNow}', {id_componente}, 1);")

    conexao.commit()

    print("=" * 100)

    return valor_risco

def atualizar_servidor(id_servidor, prioridade):
    sql = f"UPDATE servidor SET prioridade = {prioridade} WHERE id_servidor = {id_servidor}"
    print(sql)
    comando.execute(sql)
    conexao.commit()

selects = login()
risco_check = None
risco = 0
risco_cpu = 0
risco_ram = 0
risco_disco = 0

while True:
    for i in selects[0]:
        if i[1] == 'CPU':
            risco_cpu = MostrarValoresCPU(i[0])
        if i[1] == 'RAM':
            risco_ram = MostrarValoresRAM(i[0])
        if i[1] == 'Disco':
            risco_disco = MostrarValoresDiscoLocal(i[0])
            
    risco = risco_cpu + risco_disco + risco_ram
    
    if risco_check == None:
        risco_check = risco
        
    if risco_check != risco:
        atualizar_servidor(selects[1][0][0], risco)
    risco_check = risco

    sleep(5)

    print('Para parar digite ctrl + c')