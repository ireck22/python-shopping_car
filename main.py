#!/usr/bin/python3.12
# -*- coding: utf-8 -*-
import sys

class bookcar:
    def __init__(self):
        self.total=[]   #這是放商品
        self.totalsum=0 #算金額用
    
    def add(self,name,price,qty): #新增項目
        sum=price*qty
        for e in range(0,len(self.total)):
            if self.total[e]['name']==name:
                self.total[e]["qty"]+=qty
                self.total[e]["sum"]+=sum
            return 1
        self.total.append({"name":name,"price":price,"qty":qty,"sum":sum})


book1=bookcar()
item1=input("請輸入商品名稱和價格和數量?")
item2=input("請輸入第二個商品名稱和價格和數量?")
item1_1=item1.split(',')
item2_1=item2.split(',')

book1.add(item1_1[0],int(item1_1[1]),int(item1_1[2]))
book1.add(item2_1[0],int(item2_1[1]),int(item2_1[2]))