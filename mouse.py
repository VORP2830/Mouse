from re import escape
import pyautogui 
from tkinter import *
import os
import sys


def mouse():
    while True:
        try:
            pyautogui.moveTo(500,500)
            pyautogui.moveRel(0, 50, duration=1)
            pyautogui.moveRel(0, -50, duration=1)
            sys.exit()
        except:
            texto_finalizado["text"] = "Aplicação desligado com sucesso!!"
            break 

janela = Tk()
janela['background'] = 'Black'
janela.title("Mouse")
janela.geometry("260x150")
texto_orientecao = Label(janela, text= "Clique no botão para acionar o mouse")
texto_orientecao.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text = "ATIVAR", command=mouse)
botao.grid(column=0, row=3, padx=10, pady=10)
        
texto_finalizado = Label(janela, text="Mexa o mouse finalizar aplicação")
texto_finalizado.grid(column=0, row=6, padx=10, pady=10)

janela.mainloop()
