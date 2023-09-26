import tkinter
from tkinter import *
from time import sleep	
from datetime import date, datetime
import psutil
from psutil import *
import os

class Teste:
    def __init__(self,root_out):
        self.root = root_out
        self.root.title('GreyCloudTransaction')
        self.root.geometry('1200x1000')
        self.widget1 = Frame(self.root, pady=0)
        
        self.labelCpu = Label(self.widget1, text='CPU', highlightbackground="black", highlightthickness=1, width=40, height=2, bg="gray", foreground="white", font=(14))
        self.labelRAM = Label(self.widget1, text='RAM', highlightbackground="black", highlightthickness=1, width=40, height=2, bg="gray", foreground="white", font=(14))
        self.labelHD = Label(self.widget1, text='HD', highlightbackground="black", highlightthickness=1, width=40, height=2, bg="gray", foreground="white", font=(14))

        self.labelCpu.grid(row=0, column=0)
        self.labelRAM.grid(row=0, column=1)
        self.labelHD.grid(row=0, column=2)

        self.labelQntdCoresThreads = Label(self.widget1, text= "inserirValor", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12), height=6)
        self.labelQntdCoresThreads.grid(row=1, column=0)

        self.labelTituloTemposCpu = Label(self.widget1, text='TEMPOS DA CPU', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        self.labelTituloTemposCpu.grid(row=2, column=0)

        self.labelTemposCpu = Label(self.widget1, text="InsirirValor", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12), height=6)
        self.labelTemposCpu.grid(row=3, column=0)

        # self.labelTituloPercentUtilizacaoCpu = Label(self.widget1, text='UTILIZACAO DA CPU', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        # self.labelTituloPercentUtilizacaoCpu.grid(row=4, column=0)

        # self.labelPercentUtilizacaoCpu = Label(self.widget1, text="inserirValor", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12))
        # self.labelPercentUtilizacaoCpu.grid(row=5, column=0)

        self.labelTituloPercentUtilizacaoThread = Label(self.widget1, text='UTILIZACAO DAS THREADS', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        self.labelTituloPercentUtilizacaoThread.grid(row=6, column=0)

        self.labelPercentUtilizacaoThread = Label(self.widget1, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12))
        self.labelPercentUtilizacaoThread.grid(row=7, column=0)

        self.labelTituloFrenquenciaCpu = Label(self.widget1, text='FREQUENCIA DA CPU', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        self.labelTituloFrenquenciaCpu.grid(row=8, column=0)

        self.labelFrequenciaCpu = Label(self.widget1, text="inserirDados", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12))
        self.labelFrequenciaCpu.grid(row=9, column=0)

        self.labelPorcentagemRAM = Label(self.widget1, text="inserirValor", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12), height=6)
        self.labelPorcentagemRAM.grid(row=1, column=1)

        self.labelTituloQuantidadeRAM = Label(self.widget1, text='QUANTIDADE MEMÓRIA RAM', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        self.labelTituloQuantidadeRAM.grid(row=2, column=1)        

        self.labelQuantidadeRAM = Label(self.widget1, text="inserirDados", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12))
        self.labelQuantidadeRAM.grid(row=3, column=1)

        self.labelPorcentagemHD = Label(self.widget1, text="InserirDados", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12), height=6)
        self.labelPorcentagemHD.grid(row=1, column=2)

        self.labelTituloQuantidadeHD = Label(self.widget1, text='MEMÓRIA DO DISCO RÍGIDO', highlightbackground="black", highlightthickness=1, width=40, font=(14), height=2, bg="gray", foreground="white")
        self.labelTituloQuantidadeHD.grid(row=2, column=2)

        self.labelQuantidadeHD = Label(self.widget1, text="inserirDados", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=40, font=(12), height=6)
        self.labelQuantidadeHD.grid(row=3, column=2)

        while True:
            sleep(2)  

            self.labelQntdCoresThreads["text"] = f"""
                Uso da CPU: {self.getDadosCPU()[0]} 
                Quantidade de Cores: {self.getDadosCPU()[2]} 
                Quantidade de Threads: {self.getDadosCPU()[3]}
            """
    
            self.labelTemposCpu["text"] = f"""
                Processos do Usuário (user): {"{:.2f}".format(self.getDadosCPU()[4].user)} s
                Processos do Sistema (system): {"{:.2f}".format(self.getDadosCPU()[4].system)} s
                Tempo Ocioso (idle): {"{:.2f}".format(self.getDadosCPU()[4].idle)} s  
            """

            self.labelPercentUtilizacaoThread['text'] = ''
            for i in range(len(self.getDadosCPU()[1])):
                  text = self.labelPercentUtilizacaoThread.cget("text") + f"\n Thread {i + 1}: {self.getDadosCPU()[1][i]} %"
                  self.labelPercentUtilizacaoThread.configure(text=text)

            

            self.labelFrequenciaCpu["text"] = f"""
                Frequência Atual: {self.getDadosCPU()[5].current} MHz
                Frequência Máxima: {self.getDadosCPU()[5].max} MHz
                Frequência Mínima: {self.getDadosCPU()[5].min} MHz
            """
            
            self.labelPorcentagemRAM["text"] = f"""
                Uso da RAM: {self.getDadosCPU()[2]} %
            """

            self.labelQuantidadeRAM["text"] = f"""
                Quantidade Total: {"{:.2f}".format(self.getDadosRAM()[2])} GB
                Quantidade Usada: {"{:.2f}".format(self.getDadosRAM()[3])} GB
                Quantidade Disponível: {"{:.2f}".format(self.getDadosRAM()[4])} GB
                Quantidade Livre: {"{:.2f}".format(self.getDadosRAM()[5])} GB
            """
            
            self.labelQuantidadeHD["text"] = f"Quantidade Total de HD: {'{:.2f}'.format(self.getDadosHD()[1])} GB\n Quantidade Em Uso do HD: {'{:.2f}'.format(self.getDadosHD()[2])} GB \n Quantidade Livre de HD: {'{:.2f}'.format(self.getDadosHD()[3])} GB"

            self.labelPorcentagemHD["text"] =f"""
                Uso do HD: {self.getDadosHD()[0]} %
            """
            self.widget1.grid()

            self.root.update()

    def getDadosCPU(self):
        porcentagemUtilizacaoCPU = psutil.cpu_percent()
        porcentagemUtilizacaoThread = []
        qtdCores = psutil.cpu_count(logical=False)
        qtdThreads = psutil.cpu_count()
        temposCpu = psutil.cpu_times()
        porcentagemUtilizacaoThread = psutil.cpu_percent(percpu=True)
        porcentagemUtilizacaoCPU = psutil.cpu_percent()
        frequenciaCpu = psutil.cpu_freq() 
        

        return [porcentagemUtilizacaoCPU,porcentagemUtilizacaoThread, qtdCores, 
                qtdThreads, temposCpu, frequenciaCpu]

    def getDadosRAM(self):
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

        return [valoresMemoriaRam, ramPercentualUtilizado, ramByteToGigabyteTotal, 
                ramByteToGigabyteUsando, ramByteToGigabyteDisponivel, ramByteToGigabyteLivre]


    def getDadosHD(self):
        totalDisco = psutil.disk_usage('/').total
        sendoUsado = psutil.disk_usage('/').used
        espacoLivre = psutil.disk_usage('/').free
        porcentagemEmUso = psutil.disk_usage('/').percent
        byteToGigabyteTotal = (float(totalDisco) * (1 * pow(10,-9)))
        byteToGigabyteUsando = (float(sendoUsado) * (1 * pow(10,-9)))
        byteToGigabyteLivre = (float(espacoLivre) * (1 * pow(10,-9)))

        return [porcentagemEmUso, byteToGigabyteTotal, byteToGigabyteUsando, byteToGigabyteLivre]
            
root = Tk()
teste = Teste(root)
root.mainloop()