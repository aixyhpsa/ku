import numpy as np

import matplotlib.pyplot as plt

def zhengxian() :
    x=np.arange(-10,10)
    y=np.cos(x)
    plt.figure(1)
    plt.subplot(111)
    plt.stem(x, y) #stem离散，plot连续
    plt.show()

def maichong():
    def function(x):
        y=x==0
        return y.astype(np.int)
    x = np.arange(-10, 10)
    y = function(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('δ(n)')
    plt.xlabel('x')
    plt.ylabel('y')
    ax1.scatter(x, y, c='b', marker='o')
    plt.legend('x1')
    plt.grid(True)
    plt.show()

def jieyue():
    def function(x):
        y = x >= 0
        return y.astype(np.int)
    x = np.arange(-10, 10)
    y = function(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('δ(n)')
    plt.xlabel('x')
    plt.ylabel('y')
    ax1.scatter(x, y, c='b', marker='o')
    plt.legend('x1')
    plt.grid(True)
    plt.show()

import tkinter as tk 
#导入tkinter并且下面用tk（任意字符）代替tkinter,如果没有“as tk”则不能代替
root=tk.Tk() #生成主窗口,root只是变量名可以随便取别的
root.title("按钮作业") #主窗口root的名字
root.geometry("200x100") #主窗口root的大小,root.geometry("长度x宽度")
l=tk.Label(root,text='离散函数按钮',bg="green",width=25) #生成标签,label(标签)
l.pack()   #将标签添加到主窗口,pack(打包封装)

b1=tk.Button(root,text='单位脉冲序列',command=maichong) #生成按钮1，button（按钮）
b1.pack()  #将button1添加到root主窗口

b2=tk.Button(root,text='单位阶跃序列',command=jieyue)
b2.pack()

b3=tk.Button(root,text='正弦信号',command=zhengxian)
b3.pack()

root.mainloop()   #必需,loop(循环)

        

