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


version = 1.0 


def EastToPrint(origin_folder,destination_folder):
    parser = argparse.ArgumentParser('create image pairs')
    parser.add_argument('--fold_A', dest='fold_A', help='input directory for image', type=str, default=str(origin_folder))
    parser.add_argument('--fold_B', dest='fold_B', help='input directory for image', type=str, default=str(destination_folder))
    args = parser.parse_args()
    
    for arg in vars(args):
        print('[%s] = ' % arg,  getattr(args, arg))
    
    splits = os.listdir(args.fold_A)
    img_fold_A = args.fold_A
    img_fold_B = args.fold_B
    if not os.path.isdir(img_fold_B):
        os.makedirs(img_fold_B)
    # binarization
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
            if len(datas) < 4:
                print ('bounding box information error')
                continue
            left = float(datas[0])
            right = float(datas[1])
            top = float(datas[2])
            bottom = float(datas[3])
            className=0
            f1.write('%d,%d,%d,%d,%d,%d,%d,%d,%s\n' % (left, top, right, top, right, bottom, left, bottom, className))
        f1.close()
        fidin.close()
            # im_AB = np.concatenate([im_A, im_B], 1)
            # cv2.imwrite(path_AB, im_AB)


def PrintToEast(origin_folder,destination_folder):
    parser = argparse.ArgumentParser('create image pairs')
    parser.add_argument('--fold_A', dest='fold_A', help='input directory for image', type=str, default=str(origin_folder))
    parser.add_argument('--fold_B', dest='fold_B', help='input directory for image', type=str, default=str(destination_folder))
    args = parser.parse_args()
    
    for arg in vars(args):
        print('[%s] = ' % arg,  getattr(args, arg))
    
    splits = os.listdir(args.fold_A)
    img_fold_A = args.fold_A
    img_fold_B = args.fold_B
    if not os.path.isdir(img_fold_B):
        os.makedirs(img_fold_B)
    # binarization
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
            if 9 != len(datas):
                print('bounding box information error')
                continue
            left = min([float(datas[0]), float(datas[2]), float(datas[4]), float(datas[6])])
            right = max([float(datas[0]), float(datas[2]), float(datas[4]), float(datas[6])])
            top = min([float(datas[1]), float(datas[3]), float(datas[5]), float(datas[7])])
            bottom = max([float(datas[1]), float(datas[3]), float(datas[5]), float(datas[7])])
            f1.write('Char\n%d\t%d\t%d\t%d\t\r\n' % (left, right, top, bottom))
        f1.close()
        fidin.close()
    

if __name__=='__main__':
    print("欢迎使用文本格式转换器v%f" % version)
    print("loading...")
    time.sleep(0.5)
    
    print('East格式转Print格式：请输入1') 
    print ('Print格式转East格式：请输入2')
    
    mode = input("选择:")
    while mode !="1" and mode !="2" : 
        print ("请输入正确选项")
        print('East格式转Print格式：请输入1') 
        print ('Print格式转East格式：请输入2')
        mode = input("选择:")
    
    if mode == "1": 
        print ("East格式转Print格式")
        origin = input('请输入源文档所在文件夹地址: ')
        destination = input('请输入目标文件夹地址: ')
        EastToPrint(origin,destination)
        
    if mode == "2": 
        print ("Print格式转East格式")
        origin = input('请输入源文档所在文件夹地址: ')
        destination = input('请输入目标文件夹地址: ')
        PrintToEast(origin,destination)