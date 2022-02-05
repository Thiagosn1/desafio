#Permite usar as funções e objetos do módulo turtle
import turtle

def desenharTartaruga(arquivo, tartaruga):
    linha = arquivo.readline()
    while linha:
        linhaArquivo = linha.split()
        
        if linhaArquivo[0] == "CIMA":
            tartaruga.penup()
            
        elif linhaArquivo[0] == "BAIXO":
            tartaruga.pendown()
            
        else:
            x,y = int(linhaArquivo[0]), int(linhaArquivo[1])
           
            tartaruga.goto(x,y)
        
        linha = arquivo.readline()

          
#Abre o arquivo       
arquivo = open("tartaruga.txt", "r")

tartaruga = turtle.Turtle()
tela = turtle.Screen()      
desenharTartaruga(arquivo, tartaruga)

#Fecha o arquivo
arquivo.close()
