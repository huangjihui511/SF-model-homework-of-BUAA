from tkinter import *
root=Tk()
label=Label(root,text='用户名:',anchor='c').grid(row=0)
En=Entry(root).grid(row=0,column=1)
label1=Label(root,text='密码  :',anchor='c').grid(row=1)
En1=Entry(root,show='*').grid(row=1,column=1)
Button(root,text='确定',anchor='c',width=6,height=1).grid(row=2,column=1)
root.mainloop()

