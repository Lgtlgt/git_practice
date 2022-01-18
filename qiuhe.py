# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:31:03 2022

@author: Administrator
"""

class sum():
    
    def __init__(self,a1, div, num):
        
        self.a1 = a1
        self.div = div
        self.num = num
    def result(self):
        res = (self.a1 + (self.a1+(self.num-1)*self.div))*self.num
        res = 0.5*res
        return res
    
practice = sum(1,1,2)
practice.result()
    