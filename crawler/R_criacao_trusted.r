install.packages("RMySQL")
install.packages("rstudioapi")

library(RMySQL)
library(rstudioapi)

setwd(dirname(getActiveDocumentContext()$path))
caminho = getwd()
caminho <- paste(caminho, "/trusted.csv", sep = "")

mysqlconnection = dbConnect(RMySQL::MySQL(),
                            dbname='prova_marise',
                            host='localhost',
                            port=3306,
                            user='aluno',
                            password='sptech')

result = dbSendQuery(mysqlconnection, "select * from registros")

data.frame = fetch(result, n=-1)

View(data.frame)

write.csv(data.frame, caminho, row.names = FALSE)
