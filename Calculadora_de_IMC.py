import tkinter as tk
from tkinter import Frame, Label, Button, Entry
from math import pow

def calcula_IMC():
    IMC = float(peso.get())/ pow(float(altura.get()),2)
    resultado['text'] = f'O seu IMC é: {IMC:.2f}'

janela = tk.Tk()
frame = Frame(janela, pady=40).grid(column=1,row=1)

Label(janela, text='Para saber seu IMC preencha os campos abaixo',pady=40).grid(column=1,row=1,columnspan=2)
Label(janela, text='Qual seu peso (kg):').grid(column=1,row=2)
peso = Entry(frame)
peso.grid(column=2,row=2)

Label(janela, text='Qual sua altura (m):').grid(column=1,row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular',command=calcula_IMC).grid(column=2,row=4)
resultado = Label(frame)
resultado.grid(column=1,row=5,columnspan=2)

janela.title('Calculadora de IMC')
janela.mainloop()