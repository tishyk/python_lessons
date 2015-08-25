#! coding: utf-8

""" On Linux computers, the scrot program needs to be installed to use the screenshot functions in PyAutoGUI.
    In a Terminal window, run sudo apt-get install scrot to install this program."""
  
import pyautogui

im = pyautogui.screenshot()
im.getpixel((200, 250)) # coord (x,y) => (130, 135, 144)

pyautogui.pixelMatchesColor(200, 250, (130, 135, 144)) #check RGB value => True
