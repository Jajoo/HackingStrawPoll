'''Kinda works but I hit a wall because I don't know anything about IP adresses yet. Will probably pick it up again.'''

import pyautogui

def newTab():
    pyautogui.moveTo(170,6)#moveing to the new tab button, make sure there is only one previous tab
    pyautogui.click()#clicking on new tab
    pyautogui.rightClick(195, 34)#right clicking
    pyautogui.moveTo(258, 132)
    pyautogui.click()

def ChooseOp1():
    pyautogui.moveTo(391, 272)#moving to option #1
    pyautogui.click()#clicking
    pyautogui.moveTo(464, 412)#moving to "VOTE"
    pyautogui.click()#clicking

def ChooseOp2():
    pyautogui.moveTo(386, 306)#moving to option #2
    pyautogui.click()#clicking
    pyautogui.moveTo(464, 412)#moving to "VOTE"
    pyautogui.click()#clicking

def ChooseOp3():
    pyautogui.moveTo(390, 347)#moving to option #3
    pyautogui.click()#clicking
    pyautogui.moveTo(464, 412)#moving to "VOTE"
    pyautogui.click()#clicking

def ChooseOp4():
    pyautogui.moveTo(391, 377)#moving to option #1
    pyautogui.click()#clicking
    pyautogui.moveTo(464, 412)#moving to "VOTE"
    pyautogui.click()#clicking

ChooseOp1()

#Shitty code by Jajoo. Feel free to use it but I don't know why you would
