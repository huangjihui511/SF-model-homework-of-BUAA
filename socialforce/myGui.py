#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter
from .simulator import Simulator

class MyGui():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, xlength = 50,ylength = 50,population = 30,deltatime = 0.05, r = 0.2, epoch = 10000,ratio = 1,expV = 2,gatewidth = 1):

        win = tkinter.Tk()
        win.title("Social Force Simulator")
        key_list = ['xlength', 'ylength', 'population', 'deltatime', 'expV', 'gatewidth']
        value_list = [xlength, ylength, population, deltatime, expV, gatewidth]
        var_list = [tkinter.DoubleVar() for i in range(len(value_list))]
        for i in range(len(var_list)):
            var_list[i].set(value_list[i])
        

        labal_list = [tkinter.Label(win, text=key_list[i], anchor='w').grid(row = i) for i in range(len(key_list))]
        entry_list =[tkinter.Entry(win,textvariable = var_list[i]).grid(row = i,column=1) for i in range(len(value_list))]


        def showinfo():
            # 获取输入的内容
            print('hello world')
            simu = Simulator(xlength = var_list[0].get(),ylength = var_list[1].get(),population = int(var_list[2].get()),deltatime = var_list[3].get(), r = 0.2, epoch = 10000,ratio = 1,expV = var_list[4].get(),gatewidth = var_list[5].get())
            simu.run(visual = True)

        button1 = tkinter.Button(win, text="Start Simulating!", command=showinfo).grid(row = len(key_list))
        button2 = tkinter.Button(win, text="Quit!", command=win.quit).grid(row = len(key_list) + 1)
        label = tkinter.Label(win, text = 'AUTHORED BY JIHUI HUANG OF BUAA')
        #text.insert(tkinter.INSERT, )
        label.grid(row = len(key_list) + 1,column=1)
        win.mainloop()
