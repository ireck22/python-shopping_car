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

    def show(self): #顯示購物車
        finish=""
        self.totalsum=0 #總金額初始化
        for d in range(0,len(self.total)):
           finish+=f"{self.total[d]['name']}-價格:{self.total[d]['price']}-數量:{self.total[d]['qty']}-小記:{self.total[d]['sum']}\n" 
           self.totalsum+=self.total[d]["sum"] #計算總金額
        finish+=f"==============共{self.totalsum}元===================="
        return finish
    
    def rv_item(self,name): #以下是移除商品
        try:
            new_total=[]
            for k in self.total:
                if name in k['name']:
                    continue
                new_total.append(k)
            self.total=new_total
            return 1
        except ZeroDivisionError as err:
            return 2
book1=bookcar()
item1=input("請輸入商品名稱和價格和數量?")
item2=input("請輸入第二個商品名稱和價格和數量?")
item1_1=item1.split(',')
item2_1=item2.split(',')

book1.add(item1_1[0],int(item1_1[1]),int(item1_1[2]))
book1.add(item2_1[0],int(item2_1[1]),int(item2_1[2]))

result=book1.show()
print(result)

book1.rv_item('java')
result2=book1.show()
print(result2)