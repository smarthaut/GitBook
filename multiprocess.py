#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/13 16:10
# @Author  : huanghe
# @Site    : 
# @File    : multiprocess.py
# @Software: PyCharm

from multiprocessing import Process
import os

def run_proc(name):
    print('子进程运行中，name= %s,pid=%d...'%(name,os.getpid()))

if __name__=='__main__':
    print('父进程%d' %os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('zi子进程将要运行')
    p.start()
    p.join()
