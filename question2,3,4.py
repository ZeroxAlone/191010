# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:19:11 2019

@author: lisa_
"""

import random
'''
#Q2

def GetTemp():
    return random.uniform(0, 100)

GetTemp()

def Alarm():
    print("Warning!")

def CheckSensor():
    LowTemp = 25
    HighTemp = 40
    while True:
        SensorID = int(input("Enter an ID: "))
        if 0 <= SensorID <= 10:
            break
    Temp = GetTemp()
    if Temp <= LowTemp:
        print("Cold")
    if Temp >= HighTemp:
        Alarm()
    if LowTemp <= Temp <= HighTemp:
        print("Normal")

CheckSensor()

#Q3

def GenerateArray():
    Array1 = []
    for i in range(100):
        Array1.append(random.uniform(0, 100))
    
    return Array1

def ScanArray():
    TotalValue = 0
    ZeroCount = 0
    Result = GenerateArray()
    for i in Result:
        if i == 0:
            ZeroCount+=1
        TotalValue+=i
    Average = TotalValue / 100
    print("The average is: ", Average)
    print("The number of elements with a value of zero is: ", ZeroCount)

ScanArray()
'''     
#Q4

def SearchFile(Name):
    StudentContact = open("StudentContact.txt", "r")
    for i in StudentContact.readlines():
        for n in range(len(i)):
            Temp = ""
            if i[n] == "*":
                Temp = i[:n]
            if Temp == Name:
                return i
            else:
                return ""         
def AddToFile(Content, Text):
    file = open(Text, "a")
    file.write(Content)
    
def ProcessArray():
    NoNumStu = 0
    ClassList = open("ClassList.txt", "r")
    for i in ClassList.readlines():
        if SearchFile(i) != "":
            AddToFile(SearchFile(i), "ClassContact.txt")
        if SearchFile == "":
            AddToFile(i + "*No number", "ClassContact.txt")
            NoNumStu+=1
    print(NoNumStu)

ProcessArray()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        