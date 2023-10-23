install.packages("rstudioapi")
library(rstudioapi)

setwd(dirname(getActiveDocumentContext()$path))
caminho = getwd()
caminho <- paste(caminho, "/trusted.csv", sep = "")

df = read.csv(caminho)

View(df)

summary(df$registro)

plot(df$registro, type='l')

barplot(tail(df$registro, 3), names.arg = tail(df$data_registro, 3))

plot(df$registro)
