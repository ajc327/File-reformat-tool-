# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:49:33 2018
@author: ifssc
"""

import os
import numpy as np
import argparse
import linecache
import time 
from itertools import islice
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox








def PrintToEast(origin_folder,destination_folder):
    global fail 
    parser = argparse.ArgumentParser('create image pairs')
    parser.add_argument('--fold_A', dest='fold_A', help='input directory for image', type=str, default=str(origin_folder))
    parser.add_argument('--fold_B', dest='fold_B', help='input directory for image', type=str, default=str(destination_folder))
    args = parser.parse_args()
    

    
    splits = os.listdir(args.fold_A)
    img_fold_A = args.fold_A
    img_fold_B = args.fold_B
    if not os.path.isdir(img_fold_B):
        os.makedirs(img_fold_B)
    # binarization
    try:
        for sp in splits:
            # img_fold_A = os.path.join(args.fold_A, sp)
            # img_fold_B = os.path.join(args.fold_B, sp)
            path_A = os.path.join(args.fold_A, sp)
            path_B=os.path.join(args.fold_B, sp)
            fidin = open(path_A,'r',encoding='gb18030', errors='ignore')
            f1 = open(path_B, 'w')
            objIndex = 0
            for line in fidin.readlines():
                # objIndex += 1
                # if objIndex % 2 == 1:
                #     continue
                # data = data.strip('\t\r\n')
                # line=line.replace(' ', '\t')
                line = '\t'.join(filter(lambda x: x, line.split(' ')))
                datas = line.split('\t')
                
                
                if len(datas) == 1:
                    continue
                elif len(datas) !=5 and len(datas)!=6: 
                    messagebox.showinfo("Error", "文件格式错误，检查文件" + sp +"\n" + str(datas))
                    raise Exception 
                    
                left = float(datas[0])
                right = float(datas[1])
                top = float(datas[2])
                bottom = float(datas[3])
                className=0
                f1.write('%d,%d,%d,%d,%d,%d,%d,%d,%s\n' % (left, top, right, top, right, bottom, left, bottom, className))
        
            f1.close()
            fidin.close()
            fail = 0 
                # im_AB = np.concatenate([im_A, im_B], 1)
                # cv2.imwrite(path_AB, im_AB)
    except: 
        fail = 1
        pass 

def EastToPrint(origin_folder,destination_folder):
    global fail
    parser = argparse.ArgumentParser('create image pairs')
    parser.add_argument('--fold_A', dest='fold_A', help='input directory for image', type=str, default=str(origin_folder))
    parser.add_argument('--fold_B', dest='fold_B', help='input directory for image', type=str, default=str(destination_folder))
    args = parser.parse_args()
    

    splits = os.listdir(args.fold_A)
    img_fold_A = args.fold_A
    img_fold_B = args.fold_B
    if not os.path.isdir(img_fold_B):
        os.makedirs(img_fold_B)
    # binarization
    try:
      
        for sp in splits:
            # img_fold_A = os.path.join(args.fold_A, sp)
            # img_fold_B = os.path.join(args.fold_B, sp)
            path_A = os.path.join(args.fold_A, sp)
            path_B=os.path.join(args.fold_B, sp)
            fidin = open(path_A,'r',encoding='gb18030', errors='ignore')
            f1 = open(path_B, 'w')
            objIndex = 0
            for line in fidin.readlines():
                data = line.strip('\r\n')
                datas = data.split(',')
                
                if len(datas) !=9: 
                    messagebox.showinfo("Error", "文件格式错误，检查文件" + sp +"\n"+ str(datas))
                    raise Exception 
                    
                
                left = min([float(datas[0]), float(datas[2]), float(datas[4]), float(datas[6])])
                right = max([float(datas[0]), float(datas[2]), float(datas[4]), float(datas[6])])
                top = min([float(datas[1]), float(datas[3]), float(datas[5]), float(datas[7])])
                bottom = max([float(datas[1]), float(datas[3]), float(datas[5]), float(datas[7])])
                f1.write('Char\n%d\t%d\t%d\t%d\t\r\n' % (left, right, top, bottom))
   
        f1.close()
        fidin.close()
        fail = 0 
    except: 
        fail = 1
        pass 
    

if __name__=='__main__':
    window = Tk()
    
    window.title("Text file format conversion tool")
    window.geometry("550x470+500+300")
    window.resizable(width = False, height = False) 
    window.configure(bg = "white")

    frame1 = Frame(window, relief = "groove", height = 50, width = 490, bd = 5 )
    frame1.place(x=30,y=90)
    
    frame2 = Frame(window, relief = "groove", height = 120, width = 490, bd = 5 )
    frame2.place(x=30,y=160)
    
    frame3 = Frame(window, relief = "groove", height = 50, width = 490, bd = 5 )
    frame3.place(x=30,y=300)
    
    
    lbl_modesel = Label(window, text = "转换模式:")
    lbl_modesel.grid(column = 1, row = 2 , padx = 40, pady= 40 )
    selected = IntVar()
    rad1 = Radiobutton(window, text = "East格式转Print格式", value =1, variable = selected)
    rad2 = Radiobutton(window, text = "Print格式转East格式", value =2, variable = selected)
    rad1. grid(column = 2, row = 2)
    rad2. grid(column = 3, row = 2)
    
    lbl_title = Label(window,bg = "white")
    lbl_title. grid(column = 2, row = 1, pady = 20)
    lbl_ti = Label(window, text = "文本文档格式转换工具",  bg = "white", font = ("Arial Bold", 20), fg= "green")
    lbl_ti. place(x=140,y =20)

    
    
    
    lbl_adress1 = Label(window, text = "输入路径:")
    lbl_adress1. grid(column = 1, row = 4, pady = 20)
    
    txt1 = Entry(window, width=30)
    txt1. grid(column = 2, row = 4)
    txt1.configure(text = "test1")
    
    
    def changefield1(text):
        txt1.delete(0,END)
        txt1.insert(0,text)
        
    def bt1click():
        newdir = filedialog.askdirectory()
        changefield1(newdir)
    
    browsebutton1= Button(window, text = "Browse", command = lambda:bt1click())
    browsebutton1. grid(column = 3, row = 4)
    
    
    
    
    lbl_adress2 = Label(window, text = "输出路径:")
    lbl_adress2.grid(column = 1, row =6, pady=5)
    txt2 = Entry(window, width=30)
    txt2. grid(column = 2, row = 6)
    
    
    def changefield2(text):
        txt2.delete(0,END)
        txt2.insert(0,text)
    
    def bt2click():
        newdir = filedialog.askdirectory()
        changefield2(newdir)
        
    
    browsebutton2= Button(window, text = "Browse", command = lambda:bt2click())
    browsebutton2.grid(column =3, row = 6)
    
    
    informationtxt =  Label(window, text = "")
    informationtxt. grid(column = 2, row = 8)
    statustxt = Label(window, text = "状态： ")
    statustxt. grid(column = 1, row = 8, padx=30, pady=50)
    
    
    def start_conversion():
        origin = txt1.get()
        target = txt2.get()
        mode = selected.get()
        if mode == 0: 
            messagebox.showinfo("Error", "请选择转换模式")
        elif mode == 1:
            EastToPrint(origin,target)
            if fail ==0:
               informationtxt.configure(text = "转换成功", fg = "green")
               print (fail)
            else: 
               informationtxt.configure(text = "转换失败", fg = "red")

        else :
            PrintToEast(origin,target)
            if fail ==0:
                informationtxt.configure(text = "转换成功", fg = "green")
            else: 
                informationtxt.configure(text = "转换失败", fg = "red")

            
    def reset_conversion():
        txt1.delete(0,END)
        txt2.delete(0,END)
        informationtxt.configure(text = "已重置")

    startbutton = Button(window, text = "开始", height =2, width = 20, command = lambda:start_conversion())
    startbutton.place(x = 100, y = 370) 
    resetbutton = Button(window, text = "重置", height =2, width = 20, command = lambda:reset_conversion())
    resetbutton.place(x = 300, y = 370)
    
    
    
    window.mainloop()
